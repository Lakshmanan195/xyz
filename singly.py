class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlyLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def add(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
        
    def display(self):
        if self.head==None:
            return
        else:
            temp=self.head
            while(temp.next!=None):
                print(temp.data)
                temp=temp.next
            print(temp.data)
sl=singlyLinkedlist()
sl.add(10)
sl.add(20)
sl.add(30)
sl.display()

