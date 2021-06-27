from functools import reduce
from typing import Deque, List
import numpy as np



#一个字符肯定是wonder  两个字符肯定不是
# class Solution:
#     def wonderfulSubstrings(self, word: str) -> int:
#         def judge(s:str) ->int:
#             res= 0
#             for c in s:
#                 res ^= ord(c)
#             if res == 0 : # 0个
#                 return 1
#             if chr(res) in s:  # 一个
#                 return 1
#             return 0
#         res = len(word)
#         # i是字串长度，从1到len()
#         for i in range(2, len(word)+1):
#         # j是下标位置
#             for j in range(len(word)+1-i):
#                 res += judge(word[j:j+i])
#         return res
            
# t = Solution()
# print(t.wonderfulSubstrings("fiabhedce"))