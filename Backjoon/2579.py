import sys

n = int(sys.stdin.readline().rstrip())
data =[0] * 300
for i in range(n):
    data[i] = (int(sys.stdin.readline().rstrip()))

stair = [0] * 300


stair[0] = data[0]
stair[1] = data[0] + data[1]
stair[2] = max(data[0]+data[2], data[1]+data[2])
for i in range(3,n):
    stair[i] = max(stair[i-3]+data[i-1] ,
    stair[i-2])+data[i]
print(stair[n-1])

"""
답지를 보고 풀었다
점화식을 찾는것이 어려웠다.
계속 dp를 풀다보니 반복되는 것이 보이는 것 같다.
"""