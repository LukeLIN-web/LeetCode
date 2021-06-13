#判断字符串s中每个字符在字符串t中的出现顺序是否为递增。算法最多只需要遍历一遍字符串s和字符串t
# 不知道怎么累计移除 的裁剪. n^2的复杂度太高.
from functools import reduce
from typing import List
import numpy as np
import copy
class Solution:
    def judge(self, s: str, p: str) ->bool:
        index = -1
        for c in p:
            index = s.find(c,index+1)
            if index ==-1 :
                return False
        return True
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        #累计移除
        n = len(removable)
        j = 0
        sl = list(s)
        for i in range(n):
            sl.pop[removable[i]-j]
            tmp = str(sl)
            if self.judge(tmp,p) == False:
                return max(i,0)
        return n-1
t = Solution()
# print(t.maximumRemovals("abcbddddd", "abcd", [3,2,1,4,5,6]))
print(t.maximumRemovals("abcacb", "ab", [3,1,0]))
# print(t.maximumRemovals("qlevcvgzfpryiqlwy","qlecfqlw",[12,5]))
