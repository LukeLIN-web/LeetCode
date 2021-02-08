#include<vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        sort(nums.begin(),nums.end());
        for(int i = 0;i < nums.size();i++){
            if(i > 0 && nums[i] == nums[i-1])
                continue;
            if(i+3 < nums.size() && nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target)
                return res;// reduce time complexity
            for(int j = i+1; j< nums.size();j++){
                // target isn't a const.
                int left = j +1;
                int right = nums.size()-1;
                if(right -2 >= 0  && nums[i]+nums[right]+nums[right-1]+nums[right-2]<target)
                    break; // reduce time complexity
                if(j > i+1 && nums[j] == nums[j-1])
                    continue;
                while(left < right){
                    if( nums[i] +  nums[j] + nums[left] + nums[right] < target ){
                        left++;
                    }
                    else if(nums[i] +  nums[j] + nums[left] + nums[right] > target) {
                        right--;
                    }
                    else{
                        res.push_back({nums[i] ,  nums[j] , nums[left] , nums[right]});
                        while(left < right && nums[left] == nums[left+1]) left++;
                        while(left < right && nums[right] == nums[right-1 ]) right--;
                        left++;
                        right--;
                    }
                }
            }
        }
        return res;
    }
};
