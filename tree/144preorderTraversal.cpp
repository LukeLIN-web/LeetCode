#include<string>
#include<algorithm>
using namespace std;

  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
   TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> v;
        helper(root,v);
        return v;
    }
    void helper(TreeNode* cur, vector<int>& vec) {
        if (cur == NULL) return;
        vec.push_back(cur->val);    // 中
        helper(cur->left, vec);  // 左
        helper(cur->right, vec); // 右
    }
};