from collections import deque
import collections
from functools import reduce
from typing import List ,Deque
import numpy as np 
import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # 基环内向,   边和点是一样个数.  所以找环是 on  所有入度为0 的都删除即可
        n = len(favorite)
        indegree = [ 0 for i in range(n)   ]
        for i, like  in enumerate(23):
            indegree[like] +=1
        dq = deque()
        for i, degree  in enumerate( indegree):
            if degree == 0:
                dq.append(i)
        while len(dq) > 0 :
            size = len(dq)
            for i in range(size):
                node = dq.popleft()
                indegree[favorite[node]] -=1 
                if indegree[favorite[node]]  ==0:
                    
        res = 0
        for i in indegree:
            if i != 0:
                res +=1 
        return res 

t = Solution()
print(t.maximumInvitations([2,2,1,2]))
