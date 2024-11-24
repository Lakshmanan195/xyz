def add(poly1,poly2,m,n):
    size=max(m,n)
    l=[0 for i in range(size)]
    for i in range(m):
        l[i]=poly1[i]
    for j in range(n):
        l[j]+=poly2[j]
    return l
def display(l):
    for i in range(len(l)):
        print(l[i],"x^",i,end=" ")
poly1=[5,3,4,1]
poly2=[1,2,3]
re=add(poly1,poly2,len(poly1),len(poly2))
display(re)