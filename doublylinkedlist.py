class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class doublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def add(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=self.tail=newnode
        else:
            self.tail.right=newnode
            newnode.left=self.tail
            self.tail=newnode
    def display(self):
        if self.head==None:
            return
        else:
            temp=self.head
            while(temp.right!=None):
                print(temp.data)
                temp=temp.right
            print(temp.data)
dl=doublyLinkedList()
dl.add(10)
dl.add(20)
dl.add(30)
dl.display()