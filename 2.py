class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
class insert:
    def __init__(self):
        self.root=None
    def insert_root(self,value):
        newnode=Node(value)
        if self.root==None:
            self.root=newnode
        else:
            self.recursive_insert(self.root,newnode)
    def recursive_insert(self,parentnode,newnode):
        if newnode.value<parentnode.value:
            if parentnode.left is None:
                parentnode.left=newnode
            else:
                self.recursive_insert(parentnode.left,newnode)
        else:
            if parentnode.right is None:
                parentnode.right=newnode
            else:
                self.recursive_insert(parentnode.right,newnode)
    def display_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))  # Print current node
            self.display_tree(node.left, level + 1, "L--- ")    # Traverse left
            self.display_tree(node.right, level + 1, "R--- ") 
# Create the binary tree
bst = insert()
bst.insert_root(10)
bst.insert_root(5)
bst.insert_root(15)
bst.insert_root(7)
bst.insert_root(3)

# Display the tree
bst.display_tree(bst.root)
