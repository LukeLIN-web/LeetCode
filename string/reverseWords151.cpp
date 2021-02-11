// 所以解题思路如下：
//     移除多余空格
//     将整个字符串反转
//     将每个单词反转
#include<string>
#include<iostream>
#include<algorithm>
using namespace std;
class Solution {
public:
    string reverseWords(string s) {
        removeExtraSpaces(s);
    //    cout << "remove spaces success !" << s; 
        int start = 0, end =0  ;
        int size = s.size();
        reverse(s,0,s.size()-1);
        cout << "reverse  all success" << s; 
        for(int k = 0 ;  k < s.size();k++ ){
            if(  k == 0 ||  (s[k] != ' ' && s[k-1] == ' ')){
                start = k;
            }
            //have space , space is div 
            if(  s[k] == ' ' && s[k-1] != ' '){
                end = k -1 ;
                reverse(s,start,end);
                 cout << "reverse  all success " << s; 
            }
            if(s[k] != ' ' && (k ==  s.size()-1) ){
                end = k ; // final word don't have space
                reverse(s,start,end);
                cout << "reverse  all success " <<  s; 
            }  
        }
        return s;       
    }
    void removeExtraSpaces(string &s){
        int slow = 0, fast = 0;
        // remove front space
        while( s[fast] == ' ' &&  fast < s.size() ){
            fast++;
        }
        while(fast < s.size() ){
            if(fast -1 >0 && s[fast-1] == s[fast] && s[fast] == ' ' ){
                fast++;
            }
            else{
                s[slow++] = s[fast++];
            }
        }//remove medium space
        if(slow -1 > 0  && s[slow -1 ] == ' '){
            s.resize(slow-1 );//remove final space
        }
        else{
            s.resize(slow);
        }
    }
    // 反转字符串s中左闭right 闭的区间[start, end]
    void reverse(string& s, int start, int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            swap(s[i], s[j]);
        }
    }
};