def solution(s):
    s = list(s)
    stack = []
    for i in s:
        if stack == []:
            stack.append(i)
            continue
        if i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if stack == []:
        return 1
    else:
        return 0

# 이 풀이도 기가 막힌듯 하다.
# def solution(s):
#     stack = []
#     for i in s:
#         stack.append(i)
#         while True:
#             if len(stack) >= 2:
#                 if stack[-1] == stack[-2]:
#                     stack.pop()
#                     stack.pop()
#                 else:
#                     break
#             else:
#                 break
#     return not stack