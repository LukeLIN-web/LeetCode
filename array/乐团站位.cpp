//可以看出while循环里判断的情况是很多的，代码里处理的原则也是统一的左闭右开。
//某乐团的演出场地可视作 num * num 的二维矩阵 grid（左上角坐标为 [0,0])，每个位置站有一位成员。乐团共有 9 种乐器，乐器编号为 1~9，每位成员持有 1 个乐器。

//为保证声乐混合效果，成员站位规则为：自 grid 左上角开始顺时针螺旋形向内循环以 1，2，...，9 循环重复排列。例如当 num = 5 时，站位如图所示
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int orchestraLayout(int num, int xPos, int yPos) {
        vector<vector<int>> vt = generateMatrix(nums);
        return vt[xPos][yPos];
    }
    vector<vector<int>> generateMatrix(int n) {
        int loop = n/2;
        int offset = 1;
        int i,j;
        int startx = 0, starty = 0;//startx is from top to bottom, starty is from left to right
        int count = 1;
        vector<vector<int>> matrix(n, vector<int>(n, 0)); // 使用vector定义一个二维数组
        while(loop--){ 
            for(j = starty;j < starty + n- offset;j++){
                if(count == 10) count = 1;
                matrix[startx][j] = count++;    
            }// left opening, right closing.
            for(i = startx;i < startx + n -offset ;i++){
                if(count == 10) count = 1;
                matrix[i][starty + n- offset] = count++;//top to bottom
            }
            for(j = starty + n -offset; j > starty; j-- ){
                if(count == 10) count = 1;
                 matrix[startx + n -offset][j] = count++;// right to left
                 
            }
            for(; i > startx; i-- ){
                if(count == 10) count = 1;
                matrix[i][starty] = count++;//bottom to top
                
            }
            startx++;     // 第二圈开始的时候，起始位置要各自加1， 例如：第一圈起始位置是(0, 0)，第二圈起始位置是(1, 1)
            starty++;
            offset += 2;   // offset 控制每一圈里每一条边遍历的长度
        }
        if(n %2 ){
            if(count == 10) count = 1;
            matrix[startx][starty] = count;    // 如果n为奇数的话，需要单独给矩阵最中间的位置赋值
        }
        return matrix;
    }
};