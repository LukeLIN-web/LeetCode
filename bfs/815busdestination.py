from functools import reduce
from typing import Deque, List
import numpy as np
from collections import defaultdict
class Solution:
    
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        def bfs()->int:
            #记录某个车站可以进入的路线
            dict = defaultdict(set)
            #队列存的是经过的路线
            dq = Deque()
            #哈希表记录的进入该路线所使用的距离
            #起始时将「起点车站」所能进入的「路线」进行入队，每次从队列中取出「路线」时，
            # 查看该路线是否包含「终点车站」：包含「终点车站」：返回进入该线路所花费的距离
            # 不包含「终点车站」：遍历该路线所包含的车站，将由这些车站所能进入的路线，进行入队
            #由于是求最短路，同一路线重复入队是没有意义的，因此将新路线入队前需要先判断是否曾经入队。
            m = defaultdict(int)
            n = len(routes)
            for i in range(n):
                for station in routes[i]:
                    #将从起点可以进入的路线加入队列
                    if station == source:
                        dq.append(i)
                        m[i] = 1
                    if station in dict:
                        s = dict[station]
                    else:
                        s = set()
                    s.add(i)
                    dict[station] = s
            while dq:
                #取出当前所在的路线，与进入该路线所花费的距离
                route = dq.popleft()
                step = m[route]
                #遍历该路线所包含的车站
                # 查看该路线是否包含「终点车站」：包含「终点车站」：返回进入该线路所花费的距离
                for station in routes[route]:
                    if station == target: return step
                    lines = dict[station]
                    #将由该线路的车站发起的路线，加入队列
                    if lines == None :continue
                    for nr in lines:
                        if not nr in m:
                            m[nr] = step+1
                            dq.append(nr)
            return -1
        if source== target: return 0
        return bfs() 
        
    


    