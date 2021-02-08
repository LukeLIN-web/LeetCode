class MyLinkedList {
public:
    /** Initialize your data structure here. */
    struct Node
    {
        int val;
        Node *next;
        Node(int val):val(val),next(nullptr){}
    };
    
    MyLinkedList() {
        dummy = new Node(0);
        size = 0;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if(index < 0 || index > size-1 ){
            return -1;
        }
        Node * p = dummy->next;
        while(index--){
            p = p->next;
        }// index = 0 return first.
        return p->val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        Node * p = dummy->next;
        Node * n = new Node(val);
        dummy->next = n;
        n->next = p;
        size++;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        Node * p = dummy->next;
        Node * n = new Node(val);
        if(p == nullptr){
            dummy->next = n;// could p = dummy, then skip this judge.
        }
        else{
            while(p->next != nullptr){
                p = p->next;
            }
            p->next = n;
        }
        size++;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        Node * p = dummy;
        Node * n = new Node(val);
        if(index < 0 || index > size){
            return;
        }
        while(index--){
            p = p->next;
        }// index = 0 return first.
        if(p->next == nullptr){
            p->next = n;
        }
        else{
            n->next = p->next;
            p->next = n;// find the node before the index-th
        }
        size++;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        Node * p = dummy;
        if(index < 0 || index > size-1){
            return;
        }
        while(index--){
            p = p->next;
        }// index = 0 return first.
        if(p->next == nullptr){
            ;// if invalid
        }
        else{
            Node* tmp = p->next;
            p->next = p->next->next;// find the node before the index-th
            delete tmp;
        }
        size--;
    }
private: 
    int size;
    Node* dummy;
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */