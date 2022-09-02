def change():
    global d 
    d -= 1
    if d == -1:
        d = 3
n, m = map(int, input().split())

x, y, d = map(int, input().split())

check = [[0]*m for _ in range(n)]
check[x][y] = 1

array = []

for _ in range(m):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turntime =0
while(True):
    change()
    nx = x + dx[d]
    ny = y + dy[d]

    if check[nx][ny] == 0 and array[nx][ny] == 0: #왼쪽 방향으로 가보지 않은 칸과 육지라면 한칸 전진
        x,y = nx, ny
        check[x][y] = 1
        count += 1
        turntime = 0
        continue
    
    else:   # 왼쪽 방향에 가보지 않은 칸이 없거나 바다라면 
        turntime += 1
    
    if turntime == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if array[nx][ny] == 1: # 뒤로 못가면 
            break
        x, y = nx, ny
        turntime = 0
print(count)
    
"""
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
"""

"""
이문제는 솔직히 배꼈다고 볼 수 있다.
문제를 이해하는데 부터 오래 걸렸고 접근을 다르게 하여 시간을 많이 버렸다.
그래도 답안지를 보며 끝까지 포기하지 않고 이해해서 풀어서 다행이다.
"""
