# from itertools import count
# import sys
# n = int(sys.stdin.readline().rstrip())
# data = []
# num = 0
# for i in range(n):
#     temp = (sys.stdin.readline().rstrip().split())
#     if temp[0] == 'push':
#         data.append(temp[1])
#     elif temp[0] == 'pop':
#         if len(data)> num:
#             print(data[num])
#             num+=1
#         else:
#             print(-1)
#     elif temp[0] == 'size':
#         print(len(data)-num)
#     elif temp[0] == 'empty':
#         if len(data) == num:
#             print(1)
#             # num = 0
#             # data = []
#         else:
#             print(0)
#     elif temp[0] == 'front':
#         try:
#             print(data[num])
#         except:
#             print(-1)
#     elif temp[0] == 'back':
#         if len(data) > num:
#             print(data[-1])
#         else:
#             print(-1)
    
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
que = deque()

for i in range(n):
    temp = (sys.stdin.readline().rstrip().split())
    if temp[0] == 'push':
        que.append(temp[1])
    elif temp[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)

    elif temp[0] == 'size':
        print(len(que))
    elif temp[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif temp[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif temp[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
    
"""
이 문제는 시간초과로 인해 풀지 못했다.
그래서 해설을 보고 풀었다. 스택은 뒤에서 값을 빼오면 끝이지면
큐는 앞에서 빼온다음 다시 정렬을 해줘야하기 때문에 시간이 오래걸린다.
그래서 deque를 사용하거나 list로 직접 잘 다루어줘야한다.
"""