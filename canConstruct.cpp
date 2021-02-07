#include<vector>
#include<unordered_map>
#include<string>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> m1;
        unordered_map<char,int>::iterator it;
        for(char i : magazine){
            m1[i]++;// it auto insert if don't have,could simplfy if it != end then it->second++ ; 
        }
        for(char j : ransomNote){
            if( (it = m1.find(j) ) !=  m1.end() ){
                if(it->second > 0)
                    it->second --;// if have 
                else{
                    return false;
                }
            }
            else{
                return false;
            }
        }
        return true;
    }
};