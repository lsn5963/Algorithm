from collections import deque
find = input()
n = int(input())
data = ([input() for _ in range(n)])
cnt = 0
for i in data:
    # i = list(set(i))
    # print(i)
    cnt += 1
    tmp = deque(find)
    tp = tmp.popleft()
    for j in i:
        if tp == j:
            # print(tp,j)

            if len(tmp) == 0:
                print("#%d YES" %(cnt))
                break
            tp = tmp.popleft()
        else:
            if j in tmp:
                print("#%d NO" %(cnt))
                break
    else:
        print("#%d NO" %(cnt))


# for i in data:
#     cnt += 1
#     tmp = deque(find)

#     for j in i:
#         if j in tmp:
#             if j != tmp.popleft():
#                 print("#%d NO" %(cnt))
#                 break

#     else:
#         if len(tmp) == 0:
#             print("#%d YES" %(cnt))
#         else:
#             print("#%d NO" %(cnt))

######강의 풀이######