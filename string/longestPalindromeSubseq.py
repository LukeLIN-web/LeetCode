# 子序列不是连续的
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        dp = [[0 for col in range(size)] for row in range(size)]
        for i in range(size):
            dp[i][i] = 1
        # dp的意义,dp[i][j] 左闭右闭 ,里面最长回文子序列的长度
        #递推公式: dp[i][j] 字符相同,就是+2,  字符不同,就是左边或者右边        #初始化, 一开始全为
        #所以从右下开始遍历.
        result = 0
        for i in range(size-1,-1,-1):
            for j in range(i+1,size,1):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])
        return dp[0][size-1]
