#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) -1
        while l <=r :    
            mid = l + (r - l )//2
            
            if nums[mid] == target:
                return True
            #如果有重复, 那就需要-1 .
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]: #这里必须是left, 不能是0, 因为有重复的
                    r=mid-1
                else:
                    # target落在右半部分无序区域内
                    l=mid+1
            else: # 右半部分是有序
                # target落在右半部分有序区域内
                if nums[mid]<target<=nums[len(nums)-1]:
                    l=mid+1
                else:
                    # target落在左半部分无序区域内
                    r=mid-1
        return False

