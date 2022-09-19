import sys
n = int(sys.stdin.readline().rstrip())

data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(1,n):
    data[i][0] += min(data[i-1][1],data[i-1][2])
    data[i][1] += min(data[i-1][0],data[i-1][2])
    data[i][2] += min(data[i-1][0],data[i-1][1])

print(min(data[n-1][0],data[n-1][1],data[n-1][2]))

"""
이것도 답지를 보면서 풀었다.
왜 이런 생각이 안나는지 모르겠다.
"""