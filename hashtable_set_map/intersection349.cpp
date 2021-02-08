#include<vector>
#include<unordered_set>
using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> s1 ;      //std::set和std::multiset底层实现都是红黑树，std::unordered_set的底层实现是哈希表， 使用unordered_set 读写效率是最高的，并不需要对数据进行排序，而且还不要让数据重复，所以选择unordered_set。
        unordered_set<int> s2(nums1.begin(), nums1.end());// init from nums1
        for(int i :nums2){
            if(s2.find(i) != s2.end()  )// find i in set1
                s1.insert(i);
        }
        return vector<int>(s1.begin(),s1.end());//可以用元素类型相同的容器来初始化 vector<T> 容器。用一对迭代器来指定初始值的范围。下面是一个示例：
    }
};