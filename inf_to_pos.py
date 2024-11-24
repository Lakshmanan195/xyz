operators=set(['+','-','/','*','^'])
priority={'+':1,'-':1,'/':2,'*':2,'^':3}
def inf_pos(expression):
    stack=[]
    output=""
    for character in expression:
        if character not in operators and character not in "()":
            output+=character
        elif character=='(':
            stack.append(character)
        elif character==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[character]<=priority[stack[-1]]:
                output+=stack.pop()
            stack.append(character)
    while stack:
        output+=stack.pop()
    return output
print(inf_pos("(a+h)-j+v"))
