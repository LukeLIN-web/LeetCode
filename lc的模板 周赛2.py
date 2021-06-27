from functools import reduce
from typing import List
import numpy as np
from queue import PriorityQueue
# 商店list存tuple ,  出来用pq 
class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.shops = [{} for i in range(n)]
        self.mnum = len(entries)
        self.out = [{} for i in range(n)]
        for entry in entries:
            self.shops[entry[0]][entry[1]] =  (tuple(entry))
        
    def search(self, movie: int) -> List[int]:
        q = []
        for shop in self.shops:
            if movie in shop:
                q.append(shop[movie])
        q.sort(key= lambda x: (x[2] ,x[0])) #prices 然后shop
        if len(q) <=5 :
            res_list = [x[0] for x in q]
            return res_list #测试一下空列表
        else:
            res_list = [q[x][0] for x in range(5)]
            return res_list
    def rent(self, shop: int, movie: int) -> None:
        lst = self.shops[shop]
        self.out[shop][movie] = lst[movie]
        del lst[movie]
    def drop(self, shop: int, movie: int) -> None:
        lst = self.out[shop]
        self.shops[shop][movie] = lst[movie]
        del lst[movie]
    def report(self) -> List[List[int]]:
        q = []
        for li in self.out:
            for o,value in li.items():
                q.append(value)
        q.sort(key= lambda x: (x[2] ,x[0],x[1])) #prices 然后shop
        if len(q) <=5 :
            res_list = [[x[0],x[1]] for x in q]
            return res_list #测试一下空列表
        else:
            res_list = [q[x][0] for x in range(5)]
            return res_list


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()


movieRentingSystem = MovieRentingSystem(3,[[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])
print(movieRentingSystem.search(1))
movieRentingSystem.rent(0, 1)
movieRentingSystem.rent(1, 2)
print(movieRentingSystem.report())
movieRentingSystem.drop(1, 2)
print(movieRentingSystem.search(2))