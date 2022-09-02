from tokenize import Triple


a, b = list(input())



row = {"a": 1, "b": 2, "c": 3,  "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

x,y  = row[a], int(b)


# dx = [[1, 1], [1, 1], [-1, -1], [-1, -1], [1, 1], [1, 1], [-1, -1], [-1, -1]]
# dy = [-1, 1, -1, 1, -1, 1, -1, 1]

dx = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
c =0
count = 0

for i in dx:
    x = x + i[0]
    y = y + i[1]

    if x <0 or x>=8 or y <=0 or y>=8: # 예외처리
        continue
    x, y = row[a], int(b)
    # 초기화 코드는 변수를 다르게 설정하면 됨
    count += 1


print(count)


"""
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
"""

"""
이 문제는 steps라는 개념을 접근하지 못했다. 얼추 생각은 해봤는데 직접적으로 똑같이 생각하지는
못했다. 하지만 이렇게 접근법을 1개씩 배워나가서 의미는 있었다.
조금만 디테일에 신경쓴다면 좋게 풀릴 것 같다.
"""
