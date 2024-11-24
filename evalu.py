operators=set(['+','-','/','*'])
def evalu(expression):
    stack=[]
    for character in expression:
        if character not in operators:
            stack.append(character)
        else:
            p=f"{stack[-2]}{character}{stack[-1]}"
            s=eval(p)
            stack.pop()
            stack.pop()
            stack.append(s)
    return stack
print(evalu("231*+9-"))