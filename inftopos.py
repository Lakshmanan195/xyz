Operators = set(['+', '-', '*', '/', '(', ')', '^']) 
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
def add(expression):
    stack=[]
    output=""
    for i in expression:
        if i not in Operators:
            output+=i
        elif i=='(':
            stack.append(i)
        elif i==')':
            while stack[-1]!='(':
                m=stack.pop()
                output+=m
            stack.pop()
        else:
            while stack and stack[-1]!='(' and Priority[i]<=Priority[stack[-1]]:
                output+=stack.pop()
            stack.append(i)
    while stack:
        output += stack.pop()
    return output
print(add("(a+v)-i+h"))