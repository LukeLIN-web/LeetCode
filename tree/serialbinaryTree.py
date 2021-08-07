# Definition for a binary tree node.
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = []
        dq = deque()
        dq.append(root)
        while dq :
            node = dq.popleft()
            if node != None:
                s.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                s.append('None')
        print(s)
        return "[" +",".join(s)+"]" 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        s = data[1:-1]
        num = s.split(",")
        root = TreeNode(num[0])
        dq = deque()
        dq.append(root)
        i = 1 
        while dq :
            node = dq.popleft()
            if num[i] != 'None':
                node.left = TreeNode(int(num[i]))
                dq.append(node.left)
            i +=1
            if num[i] != "None":
                node.right = TreeNode(int(num[i]))
                dq.append(node.right) 
            i +=1
        return root
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))