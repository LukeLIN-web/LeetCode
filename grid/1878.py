from collections import deque
from typing import List
from queue import PriorityQueue
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # one = 0
        # two = 0
        # three = 0
        m = len(grid)
        n = len(grid[0])
        q = PriorityQueue(3)
        def getmax(i,j) -> int:
            k = 0
            re = 0
            while i -k >= 0 and i+k <m and j +k < n and j -k >=0:
                sum = 0
                for a in range(k):
                    sum += grid[i-k+a][j-a] # i-k,j  -> i, j-k
                for a in range(k):
                    sum += grid[i+a][j-k+a] #i,j-k -> i+k,j  不能同一个地方启动, 要四个点分别启动
                for a in range(k):
                    sum += grid[i+k-a][j+a] # i+k,j -> i,j+k
                for a in range(k):
                    sum += grid[i-a][j+k-a]# i, j+k -> i-k ,j 
                if k == 0:
                    sum = grid[i][j]
                re = max(sum,re)
                k+=1 
            return re
        for i in range(m):
            for j in range(n):
                getm = getmax(i,j)
                if q.full():
                    old = q.get()
                    if old >= getm:
                        q.put(old)
                    else:
                        q.put(getm)
                else:
                    q.put(getm)
        res= [] #没必要前面搞很久处理重复
        res.append(q.get())
        if not q.empty():
            q1 = q.get()
        if res[0] != q1:
            res.insert(0,q1)
        if not q.empty():
            q1 = q.get()
        if  res[0] != q1 and res[1] != q1: #empty 不加()是出错的
            res.insert(0,q1)
        return res
                
t = Solution()
#print(t.getBiggestThree([[1,2,3],[4,5,6],[7,8,9]]))
print(t.getBiggestThree([[7,7,7]]))
