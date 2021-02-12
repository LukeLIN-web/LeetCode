#include<vector>
#include<deque>
using namespace std;
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();// 不用写很多次nums.size()，写起来快
        deque<int> q;
        for (int i = 0; i < k; ++i) {
            while (!q.empty() && nums[i] >= nums[q.back()]) {
                q.pop_back();// 在右边而且比back大， 所以可以永久移除。
            }
            q.push_back(i);
        }

        vector<int> ans = {nums[q.front()]};
        for (int i = k; i < n; ++i) {
            while (!q.empty() && nums[i] >= nums[q.back()]) {
                q.pop_back();// 在右边而且比back大， 所以可以永久移除。
            }
            //将新的元素与队尾的元素相比较，如果前者大于等于后者，那么队尾的元素就可以被永久地移除，我们将其弹出队列。我们需要不断地进行此项操作
            //，直到队列为空或者新的元素小于队尾的元素。
            q.push_back(i);
            while(!q.empty() && q.front() <= i-k ){
                q.pop_front();
            }
            ans.push_back(nums[q.front()]);
            //此时的最大值可能在滑动窗口左边界的左侧，
            //并且随着窗口向右移动，它永远不可能出现在滑动窗口中了。因此我们还需要不断从队首弹出元素，直到队首元素在窗口中为止。
        }
        return ans;
    }
};