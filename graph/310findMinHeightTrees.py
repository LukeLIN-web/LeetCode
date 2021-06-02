# 从度最小的慢慢往里面挪
# 一个度数组, 一个表示图. 
# 找到入度为1的
# 然后层序遍历.
from collections import deque
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        if(n == 1):
            res.append(0)
            return res
        degree = [0 for i in range(n)]
        adjcent = [[] for i in range(n)]
        for list in edges:
            degree[list[0]] +=1
            degree[list[1]] +=1
            adjcent[list[0]].append(list[1])
            adjcent[list[1]].append(list[0])
        dq = deque([])
        for i in range(n):
            if(degree[i]==1):
                dq.appendleft(i)
        while len(dq) != 0:
            res = []
            size = len(dq)
            for i in range(size):
                node = dq[0]
                res.append(node)
                neighbors = adjcent[node]
                for neighbor in neighbors:
                    degree[neighbor] -= 1    #我们要把度-1 , 然后如果叶子结点就入队.
                    if degree[neighbor] == 1:
                        dq.append(neighbor) #不是又把 1的连接了吗?
                dq.popleft()
        return res
t = Solution()
w = t.findMinHeightTrees(4,[[1,0],[1,2],[1,3]])
print(w)