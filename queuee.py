class queuee:
    def __init__(self,maxsize):
        self.queue=[]
        self.maxsize=maxsize
    def enqueue(self,data):
        if len(self.queue)==self.maxsize:
            print("overflow")
        else:
            self.queue.append(data)
    def dequeue(self):
        if len(self.queue)==0:
            print("queue is empty")
        else:
            print("deleted element",self.queue.pop(0))
    def display(self):
        print(self.queue[0],"<--front")
        for i in range(1,len(self.queue)-1):
            print(self.queue[i])
        print(self.queue[-1],"<--rare")
q=queuee(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.display()
q.dequeue()
q.display()
