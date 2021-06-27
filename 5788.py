from functools import reduce
from typing import List
import numpy as np
#则a1和a3之差可以表示为:b1+b2,注意是连续子序列和的绝对值最小
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:


t = Solution()

print(t.minDifference([4,5,2,2,7,10],[[0,5]]))