import sys
n = int(sys.stdin.readline().rstrip())

data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

sum = 0
temp = 0
for i in range(n):
    sum += data[i] 
    temp += sum

print(temp)

"""
이문제는 쉬웠던것 같다.
"""