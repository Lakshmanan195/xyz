Operators = set(['+', '-', '*', '/', '(', ')', '^'])
def do(expression):
    stack=[]
    for character in expression:
        if character not in Operators:
            stack.append(character)
        else:
            for i in Operators:
                if i==character:
                    p=f"{stack[-2]} {character} {stack[-1]}"
                    s=eval(p)
                    stack.pop()
                    stack.pop()
                    stack.append(s)
    return stack
st=do("231*+9-")
print(st)



