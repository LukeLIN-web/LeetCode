#include<vector>
#include<unordered_map>
using namespace std;
// slide window.
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int i = 0,j = 0;
        int sum = 0;
        int sublength = 0,result =INT32_MAX;
        for(i = 0;i < nums.size();i++){
            sum += nums[i];
            while(sum >= s){
                sublength = i - j + 1;
                result = result > sublength? sublength: result;
                sum -= nums[j++];
            }
        }
        if (result == INT32_MAX)
        {
            return 0 ;
        }
        else
        {
            return result;
        }
    }
};