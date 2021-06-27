from functools import reduce
from typing import Deque, List
import numpy as np
# 展开成一维
# 这题目不能dp的, 因为不是重复子问题. 状态是强制转移的.是图
#代码实现时，我们可以用一个队列来存储搜索状态，初始时将起点状态 (1,0)加入队列，表示当前位于起点 1，移动次数为 0。
# 然后不断取出队首，每次取出队首元素时扩展新状态，即遍历该节点的出边，若出边对应节点未被访问，则将该节点和移动次数加一的结果作为新状态，加入队列。如此循环直至到达终点或队列为空。

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        bod = [ ]
        bod.append(0) # 1对应1 ,之后就不用-1
        flag= True
        # 二维转一维
        for i in range(n-1,-1,-1):
            if flag :
                for j in range(n):
                    bod.append(board[i][j])
            else:
                for j in range(n-1,-1,-1):
                    bod.append(board[i][j])
            flag = not flag
        area = len(bod)
        # bod是一维
        if area <= 7: #考虑很短的情况
            return 1
        dq = Deque()
        visit = set() # 找没访问过的最短路径
        visit.add(1)
        dq.append((1,0))
        while dq :
            idx,num = dq.popleft()
            for i in range(1,6+1):
                next = idx+i # 定义下一个状态
                if next> area-1:
                    break
                if bod[next] >0:
                    next = bod[next] #强制传送
                if next == area -1:
                    return num+1
                if next  not in visit:
                    dq.append((next,num+1))
                    visit.add(next)
        return -1
        
t = Solution()
# print(t.snakesAndLadders([
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]))
# print(t.snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))
print(t.snakesAndLadders([[-1,-1,-1],[-1,9,8],[-1,8,9]]))
