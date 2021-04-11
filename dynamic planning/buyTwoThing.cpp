// 小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。
// 注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
//dp [n]  n元可以买几种
//target - nums[i] >   可不可以先sort,   dp[i] = dp[i]+1;// 两个到底怎么处理啊搞不懂了. 
// 初始化为0
//组合问题, 那就是先物品再背包.
//递归顺序从左到右.


class Solution {
public:
    int purchasePlans(vector<int>& nums, int target) {
        int dp[] = 
        for(int i = 0 ; i < nums.size(); i ++){
            for(int j = 0 ; j < target; j ++){
                if()

            }
        }

            
    }
};