from collections import deque, Counter
import collections
from functools import reduce
from typing import List ,Deque
import numpy as np 
import heapq
import re
import bisect
import copy
import sortedcontainers
import math
class TreeNode:
    def __init__(self, val=0, 
    left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
 

t = Solution()
print(t.replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825]) )