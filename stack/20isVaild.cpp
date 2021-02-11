#include<string>
#include<algorithm>
#include<stack>
using namespace std;
class Solution {
public:// analyze  , three situation, left more , right more , number equal but type mismatch
    bool isValid(string s) {
        stack<int> st;
        for(int i =0;i < s.size();i++){
            char tmp = s[i];
            if(tmp == '[' ||  tmp == '{' || tmp == '('){
                st.push(tmp);
            }
            else if (tmp == ']'){
                if(st.empty() || st.top()  != '[')
                    return false;
                else
                    st.pop();
            }
            else if (tmp == '}'){
                if(st.empty() || st.top()  != '{')
                    return false;
                else
                    st.pop();
            }
            else{
                if(st.empty() || st.top()  != '(')
                    return false;
                else
                    st.pop();
            }
        }
    if(st.empty()){
        return true;
    }
    else 
        return false;
    }
};