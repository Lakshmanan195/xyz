class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sttack:
    def __init__(self,maxsize):
        self.head=None
        self.tail=None
        self.maxsize=maxsize
    def push(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=self.tail=newnode
        self.tail.next=newnode
        self.tail=newnode
    def popo(self):
        if self.head is None:
            print("stack is empty")
        else:
            temp=self.head
            while(temp.next!=None):
                prev=temp
                temp=temp.next
            print("deleted element=",temp.data)
            prev.next=None
    def peek(self):
        if self.head is None:
            print("stack is empty")
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            print("peek=",temp.data)
            print("peek=",self.tail.data)
    def display(self):
        temp=self.head
        while(temp.next!=None):
            print(temp.data)
            temp=temp.next
        print(temp.data)
st=sttack(4)
st.push(4)
st.push(3)
st.push(2)
st.push(1)
st.push(0)
st.popo()
st.display()