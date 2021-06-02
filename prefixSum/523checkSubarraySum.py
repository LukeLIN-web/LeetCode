from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n <2 :
            return False
        dict = {nums[0] %k: 0,0:-1}
        prefix = []
        prefix.append(nums[0])
        for i in range(1,n,1):
            tmp = (prefix[i-1]+nums[i])%k
            prefix.append(prefix[i-1]+nums[i])
            if tmp in dict:
                if i - dict[tmp] >=2:
                    return True 
            else:
                dict[tmp] = i# 插入
        return False
t = Solution()
# print(t.checkSubarraySum([23,2,6,4,7],6))
# print(t.checkSubarraySum([23,2,4,6,7],6))
# print(t.checkSubarraySum([23,2,4,6,6],7)) # 考察0到n,所以要插入 0,-1到map
# print(t.checkSubarraySum([0],1))
# print(t.checkSubarraySum([23,2,6,4,7],13))
print(t.checkSubarraySum([1,3,6,0,9,6,9],7)) # 应该是true, 6 0 9 6
