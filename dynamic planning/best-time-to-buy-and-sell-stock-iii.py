#给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
#设计一个算法来计算你所能获取的最大利润。注意：你最多两次交易
# 。一天一共就有五个状态， 0. 没有操作
# 第一次买入
# 第一次卖出
# 第二次买入
# 第二次卖出
# dp[i][j]表示第i天状态j所剩最大现金。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 0 : return 0
        dp = [[0 for col in range(5)] for row in range(size)]
        dp[0][3] -= prices[0]
        dp[0][1] -= prices[0]
        for i in range(1,size,1):
            dp[i][0] = dp[(i-1)][0]#no op
            dp[i][1] = max(dp[(i-1)][1],-prices[i]+dp[(i-1)][0])#
            dp[i][2] = max(dp[(i-1)][2],prices[i]+dp[(i-1)][1])
            dp[i][3] = max(dp[(i-1)][3],-prices[i]+dp[(i-1)][2])
            dp[i][4] = max(dp[(i-1)][4],prices[i]+dp[(i-1)][3])
        return dp[size-1][4]