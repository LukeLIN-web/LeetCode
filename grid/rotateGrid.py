from functools import reduce
from typing import List
import numpy as np

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l, r, t, b = 0, len(grid[0]) - 1, 0, len(grid) - 1
        def rorate(l:int,r:int,t:int,b:int)->None:
            while True:
                # shang
                lt = grid[l][t]
                for i in range(l, r ):
                    grid[t][i] = grid[t][i+1]
                # zuo
                lb = grid[b][l]
                for i in range(b, t,-1 ): # 逆序遍历不然会覆盖.
                    grid[i][l] = grid[i-1][l]
                grid[t+1][l]  = lt
                # xia
                br = grid[b][r] #保存
                for i in range(r,l+1,-1  ):
                    grid[b][i] = grid[b][i-1]
                grid[b][l+1] =  lb #赋值
                # you 
                tr = grid[t][r] #保存
                for i in range(t,b ):
                    grid[i][r] = grid[i+1][r]
                grid[b-1][r] =  br #赋值
                l, r,b,t = l+1,r-1,b-1,t+1 #有的+1有的-1
                if l >r or t > b: break 
        for i in range(k):
            l, r, t, b = 0, len(grid[0]) - 1, 0, len(grid) - 1
            rorate(l,r,t,b)
        #print(grid)
        return grid


t = Solution()
print(t.rotateGrid([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],2))