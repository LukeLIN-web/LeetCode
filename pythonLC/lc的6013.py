from collections import deque, Counter
import collections
from functools import reduce
from typing import List ,Deque
import numpy as np 
import heapq
import re
import bisect
import copy
class TreeNode:
    def __init__(self, val=0, 
    left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        


t = Solution()
print(t.repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt",1) )
# "zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba"
# print(t.repeatLimitedString("robnsdvpuxbapuqgopqvxdrchivlifeepy",2) )