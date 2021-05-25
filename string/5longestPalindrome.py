   def extend(self,s1:str, i:int, j : int, n : int,max :int) -> int:
        res= ""
        l = -1
        r = -1
        while i >=0 and j < n and s1[i] == s1[j]:
            i -=1
            j +=1
            if j-i > max :
                l = i
                r = j
        return l,r
    def longestPalindrome(self, s: str) -> str:
        size =len(s)
        max = 1
        s1 = ""
        for i in range(size):
            l1,r1 = self.extend(s,i,i,size,max)
            print("l1,r1 =")
            print(l1,r1)
            l2,r2 = self.extend(s,i,i+1,size,max)
            print("l2,r2 =")
            print(l2,r2)
            if r2-l2 >= max:
                max = r2-l2 
                s1 = s[l2+1:r2] # 截取是左闭右开
            if r1-l1 >= max:
                max = r1-l1
                s1 = s[l1+1:r1]
        return s1
