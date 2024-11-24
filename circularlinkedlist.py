class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def add(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=self.tail=newnode
            newnode.next=self.head
        else:
            self.tail.next=newnode
            newnode.next=self.head
            self.tail=newnode
    def display(self):
        if self.head==None:
            return
        else:
            temp=self.head
            while(temp.next!=self.head):
                print(temp.data)
                temp=temp.next
            print(temp.data)
sc=circularLinkedList()
sc.add(10)
sc.add(20)
sc.add(30)
sc.display()