#
#难点：　怎么ｈａｓｈ？哈希表存储每个前缀和第一次出现的下标。
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0 
        dict = {0:-1}
        max = 0
        for i in range(0,n,1):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count in dict:
                if max < i- dict[count]:
                    max =   i- dict[count]
            else:
                dict[count] = i
        return max
t = Solution()
w = t.findMaxLength([0,0,1,0,0,0,1,1])
print(w)
w = t.findMaxLength([0,1])
print(w)
w = t.findMaxLength([1,0])
print(w)
                        


