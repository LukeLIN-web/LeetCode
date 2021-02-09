#include<string>
#include<algorithm>
using namespace std;
class Solution {
public:
    string replaceSpace(string s) {
        int count = 0; // 统计空格的个数
        int sOldSize = s.size()-1;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') {
                count++;
            }
        }
        s.resize(s.size() + count * 2); // 1 space  to 3 char
        int sNewSize = s.size()-1 ;
        while(sOldSize < sNewSize ){
            if(s[sOldSize] == ' ' ){
                s[sNewSize--] = '0';
                s[sNewSize--] = '2';
                s[sNewSize--] = '%';
                sOldSize--;
            }
            else{
                s[sNewSize] = s[sOldSize] ;
                sNewSize--;
                sOldSize--;
            }
        }
        return s;
    }
};

