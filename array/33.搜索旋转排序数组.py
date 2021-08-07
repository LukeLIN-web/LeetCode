#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r=0,len(nums)-1
        # 这里控制条件取等号，取等号大多是为了在while中直return mid，不取等号就跳出while返回l的值。
        while l<=r:
            mid=l+(r-l)//2
            # 中间值即为target，直接返回
            if nums[mid]==target:
                return mid
            # 左半部分是有序
            if nums[0]<= nums[mid]:# 包括mid
                if nums[0]<= target <nums[mid] :
                    r=mid-1
                else:
                    # target落在右半部分无序区域内
                    l=mid+1
            else: # 右半部分是有序, 也包括mid
                # target落在右半部分有序区域内
                if nums[mid]<target<=nums[len(nums)-1]:
                    l=mid+1
                else:
                    # target落在左半部分无序区域内
                    r=mid-1
        return -1





