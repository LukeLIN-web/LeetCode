//可以看出while循环里判断的情况是很多的，代码里处理的原则也是统一的左闭右开。
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int loop = n/2;
        int offset = 1;
        int i,j;
        int startx = 0, starty = 0;//startx is from top to bottom, starty is from left to right
        int count = 1;
        vector<vector<int>> matrix(n, vector<int>(n, 0)); // 使用vector定义一个二维数组
        while(loop--){ 
            for(j = starty;j < starty + n- offset;j++){
                matrix[startx][j] = count++;    
            }// left opening, right closing.
            for(i = startx;i < startx + n -offset ;i++){
                matrix[i][starty + n- offset] = count++;//top to bottom
            }
            for(j = starty + n -offset; j > starty; j-- ){
                 matrix[startx + n -offset][j] = count++;// right to left
            }
            for(; i > startx; i-- ){
                matrix[i][starty] = count++;//bottom to top
            }
            startx++;     // 第二圈开始的时候，起始位置要各自加1， 例如：第一圈起始位置是(0, 0)，第二圈起始位置是(1, 1)
            starty++;
            offset += 2;   // offset 控制每一圈里每一条边遍历的长度
        }
        if(n %2 ){
            matrix[startx][starty] = count;    // 如果n为奇数的话，需要单独给矩阵最中间的位置赋值
        }
        return matrix;
    }
};