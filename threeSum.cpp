#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(),nums.end());
        for(int i = 0 ; i < nums.size();i++){
            if(nums[i] > 0 )
                return res;
            int left = i+1;
            int right = nums.size()-1;
            if( i>0 && nums[i] == nums[i-1]){
                continue;// simliar with nums[i-1] process
            }
            while(left < right){
                if(nums[left] + nums[right] + nums[i] > 0){
                    right--;// judge one by one . so we use else if
                }
                else if(nums[left] + nums[right] + nums[i] == 0 ){
                    res.push_back({nums[i],nums[left], nums[right]});
                    while(left < right && nums[left] == nums[left+1]) left ++;
                    while(left < right && nums[right] == nums[right-1]) right--;
                    left++;//don't identical  
                    right --;
                } 
                else{  // <0 
                    left ++;
                }
            }
        }
        return res;
    }
};