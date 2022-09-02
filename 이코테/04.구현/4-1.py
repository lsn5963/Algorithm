n = int(input())
data = input().split()
x,y = (1,1)

for  r in range(len(data)):
    if data[r] == 'L':
        if y ==1: # continue if문은 예외처리를 하는 부분이다.
            continue 
        y -= 1
    if data[r] == 'R':
        if y == n: 
            continue
        y += 1
    if data[r] == 'U':
        if x == 1:
            continue
        x -= 1
    if data[r] == 'D':
        if x == n:
            continue
        x += 1

print(x,y)

"""
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]

    if nx> n or nx < 1 or ny > n or ny <0 :
        continue;

    x = nx;
    y = ny;



print(x, y)
"""

"""
코드를 너무 쉽게 짠 것 같다.
답지를 보면 dx와 dy값을 먼저 저장해둔 다음 해결을 한다.
다음에는 이런 접근법을 사용해야겠다.
"""
