# 遇到字符, 就开始str , 遇到空格, 就结束
class Solution:
    def reverseWords(self, s: str) -> str:
        st = []
        s += " "
        str = ""
        n = len(s)
        i = 0 
        while i < n:
            #print(i)  
            if s[i] == ' ':
                if str != "": #如果是空格继续找字符
                    st.append(str)
                    #print(str)
                    str = "" 
            else:
                str += s[i] 
                #print(str)               
            i += 1
        res = ""
        while len(st) >0:
            res += st.pop()
            res += " "
        return res.strip()
                
        
                