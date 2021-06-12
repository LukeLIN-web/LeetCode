class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        str = ""
        i = 0
        while i <  len(s):
            if s[i].isdigit() :
                print("s[i].isdigit()]")
                digit = ""
                j = i
                while(s[j].isdigit()):
                    print("digit += s[j]")
                    digit += s[j]
                    j +=1
                i = j
                st.append((int(digit),str )) # 增加2 
                print((int(digit),str ))
                str = ""
                 #跳过 [
            elif s[i] == ']':
                tuple = st.pop()
                print(tuple)
                mul = tuple[0] 
                tmp = tuple[1] 
                str1 =  str
                for j in range(mul-1):
                    str = str + str1
                str = tmp +str
            elif s[i] == '[':
                pass
            else:
                str += s[i]
            i+=1
        return str
    #print(decodeString("3[a]2[bc]"))
t = Solution()
print(t.decodeString("10[we]"))
            

