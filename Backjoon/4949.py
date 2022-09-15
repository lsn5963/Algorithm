import sys
sr = " "

while(True):
    sr = list(sys.stdin.readline().rstrip())
    stk = []
    if sr[0] == '.' and len(sr) == 1:
        break
    for i in sr:
        if i == '[':
            stk.append("[")
        if i == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                print("no")
                break
        if i == '(':
            stk.append("(")
        if i == ')':
            if stk and stk[-1] == '(' :
                stk.pop()
            else:
                print("no")
                break
    else:
        if stk:
            print("no")
        else:
            print("yes")
    
"""
스택으로 풀어야한다.
조언을 얻긴했지만 구현을 스스로 하여 뿌듯하다.
"""