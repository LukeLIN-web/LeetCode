from functools import reduce
from typing import List
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7

        # 容斥原理 g <= n, p >= minProfit的组合个数为 g<=n的个数减去g<=n,p < minProft的个数
        # 先求 g<=n 的组合数
        dp1 = [0] * (n+1)
        dp1[0] = 1
        for g in group:
            for i in range(n,g-1,-1):
                dp1[i] += dp1[i-g]
        # p < minProfit的组合数为0
        if minProfit <=0:
            return sum(dp1) % mod
        
        # 求 group <= n, profit < minProfit的组合数
        dp2 = [[0] * minProfit for _ in range(n+1)]
        dp2[0][0] = 1
        for g,p in zip(group, profit): #zip可以两个同时遍历
            for i in range(n,g-1,-1):
                for j in range(minProfit-1,p-1,-1):
                    dp2[i][j] = dp2[i][j]+  dp2[i-g][j-p]
        return (sum(dp1) - sum(sum(dp2[i]) for i in range(n+1))) % mod

t = Solution()
print(t.profitableSchemes(5,10,[2,2,1],[2,3,4]))