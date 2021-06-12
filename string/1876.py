class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        if n <= 2:
            return 0
        l = 0
        r = 1
        while r < n and s[r] == s[l]:
            l +=1 
            r+=1
        # 找到第一个不等于的 
        if r == n:
            return 0 #全部重复
        #set = {s[l]}
        r+=1
        while r < n:
            if s[r] != s[l] and s[r] != s[l+1] and s[l] != s[l+1]:
                res+=1
                print([s[l],s[r]])
            l +=1 
            r+=1 
        return res 
            #if r in set:

t = Solution()
print(t.countGoodSubstrings("xyzzaz"))

