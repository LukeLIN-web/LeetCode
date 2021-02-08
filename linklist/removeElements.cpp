 struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};
//  test point :  continus 2 delete , only one delete.
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode();
        dummy->next = head;
        ListNode* p = dummy;
        ListNode* pn = p->next;
       // while(p != nullptr){
            while(pn != nullptr ){
                if(pn->val == val ){
                    ListNode* tmp = pn;
                    p->next = pn->next;
                    delete tmp;
                    pn = p->next;
                }
                else{
                    p = pn;
                    pn = p->next;
                }            
            }
        return dummy->next;
    }
};