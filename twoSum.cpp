#include<vector>
#include<unordered_map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        vector<int> tmp;
        unordered_map <int,int> map;
        for(int i = 0 ; i < nums.size(); i++){
            auto it = map.find(target- nums[i]);
            if(it != map.end()  ){
                return {it->second,i}; //find it    
            }
            map.insert(nums[i],i);  // 否则你插入继续chaxun
        }
        return {};
    }
};
