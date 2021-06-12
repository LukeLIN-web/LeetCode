from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        cnt = [[0 for i in range(2)] for j in range(size) ]
        for i in range(size):
            a= 0
            b=0
            for c in strs[i]:
                if c == '1':
                    a +=1
                else:
                    b+=1
            cnt[i][0] = b
            cnt[i][1] = a
        dp = [[[0 for i in range(n+1)]for j in range(m+1)]for k in range(size+1)]
        for i in range(1,size+1,1):
            zero = cnt[i-1][0]
            one = cnt[i-1][1]
            for j in range(m+1):
                for k in range(n+1):
                    a = dp[i-1][j][k]
                    if j >= zero and k>= one:
                        b = dp[i-1][j-zero][k-one] +1
                    else:
                        b = 0
                    #print(i,j,k)
                    dp[i][j][k] = max(a,b)
        return dp[size][m][n]
                    
t = Solution()
print(t.findMaxForm(["10", "0001", "111001", "1", "0"],  5,  3))
