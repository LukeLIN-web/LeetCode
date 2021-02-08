#include<vector>
#include<unordered_map>
using namespace std;
//而这道题目是四个独立的数组，只要找到A[i] + B[j] + C[k] + D[l] = 0就可以，不用考虑有重复的四个元素相加等于0的情况，所以相对于题目18. 四数之和，题目15.三数之和，还是简单了不少！」
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int,int> m1;// <两数之和,次数>
        for(int i : A){
            for(int j : B){
                m1[i+j]++;
            }
        }
        // 0 - i - j
        int count = 0;
        unordered_map<int,int>::iterator  it;
        for(int i : C){
            for(int j :D){
                if( (it =  m1.find(0-i-j) ) != m1.end()  ){
                    count += it->second;// if 0-i-j in it , add up
                }
            }
        }
        return count;
    }
};