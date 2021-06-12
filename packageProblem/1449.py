#就是一个背包问题, 首先 背包, 然后物品.
# 首先研究 target = 3可以有哪些,然后 5可以花掉3 +2的cost, 也可以花掉 2 +3 的cost.
# 因为无限背包所以dp[i]
# 背包的 过程要注意, 从0 肯定是刚好的, 一个是从之前花掉的预算中加,因为要刚好所以如果之前预算没有刚好, 就不继续探索target
# 因为j就是逐渐变大的,所以这样总把大数排第一个
# 因为位数越多越好, 所以我们先加位数然后排序

from functools import reduce
from typing import List
import numpy as np
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        n = len(cost)
        dp = ["" for i in range(target+1)]
        dp[0] = "" #一开始不需要
        for i in range(target+1): # 先背包后物品
            for j in range(9):
                if (i > cost[j] and dp[i-cost[j]] != "") or i==cost[j]: #一个是从0 肯定是刚好的, 一个是从之前花掉的预算中加,因为要刚好所以如果之前预算没有刚好, 就不继续探索target
                    if len(dp[i]) < len(dp[i-cost[j]])+1:
                        dp[i] = str(j+1) + dp[i-cost[j]]  # 因为j就是逐渐变大的,所以这样总把大数排第一个
                    if   len(dp[i]) == len(dp[i-cost[j]])+1 and dp[i][0] < str(j+1):
                        dp[i] = str(j+1) + dp[i-cost[j]]
        s = dp[target]
        l1 = list(s)
        l1.sort(reverse=True ) # 因为位数越多越好, 所以我们先加位数然后排序
        s1 = "".join(l1)
        if s1 == "": 
            return "0"
        return s1
t = Solution()
print(t.largestNumber([4,3,2,5,6,7,2,5,5],9))