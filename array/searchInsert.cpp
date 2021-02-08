#include<vector>

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        int left = 0;
        int right = n-1;
        int mid = 0;
        while(left <= right){  // 当left==right，区间[left, right]依然有效
            mid  = left + ((right - left) / 2);// 防止溢出 等同于(left + right)/2;
            if(nums[mid] < target){
                left = mid+1;// [mid+1,right]
            }
            if(nums[mid] > target){
                right = mid -1;//[left,mid-1]
            }
            if(nums[mid] == target){
                return mid;
            }
        }
        //[0,-1], return 0 然后你一通化简会发现可以都是left.
        //最右边[ n-1,n] return left
        // 中间 [right, left] return left
        return left;
    }
};