arr=[1,2,3,4,5]
#stack
def push(data):
    arr.append(data)
def POP():
    arr.pop()
def peek():
    print(arr[-1])


#queue
def enqueue(data):
    arr.append(data)
def dequeue():
    print(arr.pop(0))
def peek():
    print(arr[-1])

#stack
print("for stack")
push(5)
push(6)
POP()
peek()
#queue
print("for queue")
enqueue(5)
enqueue(7)
dequeue()
peek()