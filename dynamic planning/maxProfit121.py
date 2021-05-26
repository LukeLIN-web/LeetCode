class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 0 : return 0
        dp = [[0 for col in range(2)] for row in range(2)]
        dp[0][0] -= prices[0]
        dp[0][1] = 0
        for i in range(1,size,1):
            dp[i%2][0] = max(dp[(i-1)%2][0],-prices[i])
            dp[i%2][1] = max(dp[(i-1)%2][1],prices[i]+dp[(i-1)%2][0])
        return dp[(size-1)%2][1]



