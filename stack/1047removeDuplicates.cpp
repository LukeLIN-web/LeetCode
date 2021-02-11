#include<string>
#include<algorithm>
#include<stack>
using namespace std;
class Solution {
public:
    string removeDuplicates(string S) {
        stack<char> st;
        for(auto it : S){
            if(st.empty() || st.top() != it  ){
                st.push(it);
            }
            else{
                st.pop();
            }
        }
        int i = 0;
        while(!st.empty()){
            S[i++] = st.top();
            st.pop();
        }
        S.resize(i);//这里S 是复制了过来 
        reverse(S.begin(),S.end());// 此时字符串需要反转一下
        return S;
    }
};

/*bool isShorter(const string &s1, const string &s2)
{
    return s1.size() < s2.size();
}这里形参是引用，所以不需要复制实参；形参是const，所以不能通过该引用形参来修改实参的值。
*/