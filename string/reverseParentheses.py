class Solution:
    def reverseParentheses(self, s: str) -> str:
        #遇到左括号, 进
        st = []
        str = ""
        for i in s:
            if i == '(':
                st.append(str)
                str = ""
            elif i == ')':
                tmp = str[::-1]
                str = st.pop()+tmp
            else:
                str += i
        return str




