 struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};

//可以使用快慢指针法，  分别定义 fast 和 slow指针，从头结点出发，
//fast指针每次移动两个节点，slow指针每次移动一个节点，如果 fast 和 slow指针在途中相遇 ，说明这个链表有环。
 //这是因为fast是走两步，slow是走一步，
 //其实相对于slow来说，fast是一个节点一个节点的靠近slow的，所以fast一定可以和slow重合。
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode * fast;
        ListNode * slow;
        fast = head;
        slow = head;
        while (fast != nullptr ){
            slow = slow->next;
            fast = fast->next;
            if(fast == nullptr)
                return nullptr;
            fast = fast->next;
            if(fast == slow)
                break;          
        }
        if(fast == nullptr)
            return nullptr;
        ListNode *pos;
        ListNode *mov;
        pos = head;
        mov = fast;
        while(pos != mov){
            pos = pos->next;
            mov = mov->next;
        }
        return  pos;
    }
};
//这就意味着，「从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点， 那么当这两个指针相遇的时候就是 环形入口的节点」。
//也就是在相遇节点处，定义一个指针index1，在头结点处定一个指针index2。
//让index1和index2同时移动，每次移动一个节点， 那么他们相遇的地方就是 环形入口的节点。