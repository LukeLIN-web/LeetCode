#include<unordered_set>
using namespace std;
class Solution {
public: //sum repeat, so isn't happly . sum = 1 ,happ.
    bool isHappy(int n) {
        unordered_set<int> s1;
        int m = n;
        s1.insert(m);
        int sum = 0 ;
        while(m != 1){
            sum = 0 ;
            while(m){
                sum += (m%10) * (m%10);
                m /= 10;
            }
            if(s1.find(sum) != s1.end()){
                return false;
            }
            s1.insert(sum);
            m = sum ;
        }
        return true;
    }
};