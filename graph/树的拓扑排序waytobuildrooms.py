from functools import reduce
from typing import List
import numpy as np


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n =  len(prevRoom) #写了self就隔离开,不写就可以通用
        sum1 = 0 
        sum1 = int(sum1)
        edge = [[0 for i in range(n)] for i in range(n) ]
        visit = [0 for i in range(n)]
        indegree = [0 for i in range(n)]
        def dfs(num:int) -> None:
            if num == n:
                sum1 +=1
                self.sum1  %= (10**9+7)
                return 
            for i in range(0,n):
                if indegree[i] == 0 and visit[i] == 0:
                    for j in range(1,n):
                        if edge[i][j] ==1:
                            indegree[j]-=1
                    visit[i] = 1
                    dfs(num+1)
                    for j in range(1,n):
                        if edge[i][j] ==1:
                            indegree[j]+=1
                    visit[i] = 0
            return 
        for i in range(1,n,1):
            edge[prevRoom[i]][i] = 1
            indegree[i] +=1
        dfs(0)
        return self.sum1 % (10**9+7)
t = Solution()
print(t.waysToBuildRooms([-1,0,0,1,2]))