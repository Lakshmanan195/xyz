class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def add(self,data):
        newnode=Node(data)
        if self.root is None:
            self.root=newnode
        else:
            self.insert_recursive(self.root,data)
    def insert_recursive(self,current_node,data1):
        if data1<current_node.data:
            if current_node.left is None:
                current_node.left=Node(data1)
            else:
                self.insert_recursive(current_node.left,data1)
        else:
            if current_node.right is None:
                current_node.right=Node(data1)
            else:
                self.insert_recursive(current_node.right,data1)
    def inorder_traversal(self,node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)
    def search(self,node,data1):
        if node is None:
            return 0
        else:
            if node.data==data1:
                return 1
            if data1<node.data:
                return self.search(node.left,data1)
            else:
                return self.search(node.right,data1)

bt=BinaryTree()
bt.add(5)
bt.add(4)
bt.add(6)
bt.add(7)
bt.inorder_traversal(bt.root)
re=bt.search(bt.root,10)
if re==0:
    print("element not found")
else:
    print("element found")
    
