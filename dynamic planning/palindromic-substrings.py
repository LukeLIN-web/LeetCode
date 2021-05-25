# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         size = len(s)
#         dp = [[False for col in range(size)] for row in range(size)]
#         # dp的意义,dp[i][j] 左闭右闭是否是回文子串. 
#         #递推公式: dp[i][j] 字符相同,如果 j-i<=1,是true, >1 就是 dp[i+1][j-1], 字符不同,就是false
#         #初始化, 一开始全为false
#         #所以从左下开始遍历.
#         result = 0
#         for i in range(size-1,-1,-1):
#             for j in range(i,size,1):
#                 if s[i]==s[j]:
#                     if j-i<=1:
#                         dp[i][j] = True
#                         result +=1
#                     else:
#                         if dp[i+1][j-1] == True:
#                             dp[i][j] = True
#                             result +=1
#         return result
#首先确定回文串，就是找中心然后想两边扩散看是不是对称的就可以了。
# 在遍历中心点的时候，要注意中心点有两种情况。
# 一个元素可以作为中心点，两个元素也可以作为中心点。
# 那么有人同学问了，三个元素还可以做中心点呢。其实三个元素就可以由一个元素左右添加元素得到，四个元素则可以由两个元素左右添加元素得到。
# 所以我们在计算的时候，要注意一个元素为中心点和两个元素为中心点的情况。
# 这两种情况可以放在一起计算，但分别计算思路更清晰，我倾向于分别计算，代码如下：
class Solution:
    def extend(self,s1:str, i:int, j : int, n : int) -> int:
        res= 0 
        while i >=0 and j < n and s1[i] == s1[j]:
            i -=1
            j +=1
            res +=1
        return res
    def countSubstrings(self, s: str) -> int:
        res = 0
        size = len(s)
        for i in range(size):
            res += self.extend(s,i,i,size)
            res += self.extend(s,i,i+1,size)
        return res

        




