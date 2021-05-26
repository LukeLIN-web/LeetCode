#给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
#设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# dp[i][0] 表示第i天持有股票所得现金。
# dp[i][1] 表示第i天不持有股票所得最多现金
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 0 : return 0
        dp = [[0 for col in range(2)] for row in range(2)]
        dp[0][0] -= prices[0]
        dp[0][1] = 0
        for i in range(1,size,1):
            dp[i%2][0] = max(dp[(i-1)%2][0],dp[(i-1)%2][1]-prices[i])#要么没买, 要么今天买了
            dp[i%2][1] = max(dp[(i-1)%2][1],prices[i]+dp[(i-1)%2][0])#要么没卖, 要么卖了
        return dp[(size-1)%2][1]