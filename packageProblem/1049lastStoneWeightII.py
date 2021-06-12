#需要考虑正负号两边时，其实只需要考虑一边就可以了，使用总和 sumsum 减去决策出来的结果，就能得到另外一边的结果。
from functools import reduce
from typing import List
import numpy as np
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        sum = reduce(lambda x,y: y+x, stones)
        
        t = sum //2
        dp = np.zeros(t+1) # dp = [0 for i in range(t+1)] 这个更快 ,大概快50-70ms
        for i in range(1,n+1,1):
            x = stones[i-1]
            for j in range(t,x-1,-1):
                dp[j] = max(dp[j],dp[j-x]+x ) #若采用倒序遍历
                #则可消除该错误我们可以从后往前遍历，这样使用前面值的时候可以保证前面的还没有计算，也就是还没有被重新赋值。代码如下
        return int(abs(sum - 2*dp[t]))

t = Solution()
print(t.lastStoneWeightII([1,2]))

# class Solution:
#     def lastStoneWeightII(self, stones: List[int]) -> int:
#         n = len(stones)
#         dp = np.zeros(shape=(n, 3010)) #可以统计一下sum然后指定范围可能还比每次3000更快
#         dp[0,stones[0]+1500] = 1
#         dp[0,-stones[0]+1500] = 1 # 小于1500一定回不去, 所以不让他小于1500
#         for i in range(1,n,1):
#             for j in range(-1500,1500,1):
#                 if dp[i-1,j+1500] ==1:
#                     if j+stones[i]+1500 <=3000:
#                         dp[i,j+stones[i]+1500 ] = 1  #如果到1500,那后面肯定要都减去了
#                     if j-stones[i] >=-1500:
#                         dp[i,j-stones[i]+1500 ] =1
#         for j in range(1500,3000,1):
#             if dp[n-1,j] == 1:
#                 return j-1500
                #return j
                    
