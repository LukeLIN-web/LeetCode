# 吃糖果,
# 前缀和, 把type前面的加起来作为一个数组. 然后检查
#   left = favday+1,  right  =  dailycap*(favday+1) 如果在范围内就可以.  
# 7 11 16 19 27   [3,2*3]  [0,7]可以 right >= 0 并且 left<=7
from typing import List
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        prefix = []
        prefix.append(candiesCount[0])
        i = 1
        while i < len(candiesCount):
            prefix.append(prefix[i-1]+candiesCount[i])
            i +=1
        for q in queries:
            favtype = q[0] 
            favday = q[1]
            dailycap = q[2]
            left = favday+1
            right = dailycap*(favday+1)
            if favtype == 0:
                if right >=0 and left <= prefix[favtype]:
                    ans.append(True)
                else:
                    ans.append(False)
            else:
                if right >prefix[favtype-1] and left <= prefix[favtype]:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans

t = Solution()
print(t.canEat([7,11,5,3,8],[[2,2,6],[4,2,4],[2,13,1000000000]]))

        
