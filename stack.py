class stack:
    def __init__(self,maxsize):
        self.max=maxsize
        self.stack=[]
    def push(self,data):
        if len(self.stack)==self.max:
            print("overflow")
        else:
            self.stack.append(data)
    def POP(self):
        if len(self.stack)==0:
            print("stack.empty")
        else:
            m=self.stack.pop()
            print("poped element=",m)
    def peek(self):
        if len(self.stack)==0:
            print("underflow")
        else:
            print(self.stack[-1])
s=stack(5)
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.push(0)
s.POP()
s.peek()