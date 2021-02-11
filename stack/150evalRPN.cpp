#include<string>
#include<algorithm>
#include<stack>
using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for(int i = 0; i < tokens.size();i++){
            string s = tokens[i];
            if(s == "+" ||  s == "-"  || s == "*" || s== "/"  ){
                int a =  st.top();
                st.pop();
                int b  = st.top();
                st.pop();
                switch(s[0]){
                    case '+' :  st.push( a+b); break;// switch 不能用string
                    case '-' :   st.push( b-a);break;
                    case '*' :   st.push( b*a);break;
                    case '/' :  st.push( b/a);
                }
            }
            else{
                st.push(stoi(s));
            }
        }
        return st.top();
    }
};