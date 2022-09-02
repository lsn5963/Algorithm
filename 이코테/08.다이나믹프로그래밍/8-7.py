import sys
n = int(sys.stdin.readline().rstrip())

data = [0]*1001

data[0] = 1
data[1] = 3

for i in range(2, n):
    data[i] = (data[i-2]*2  + data[i-1])%796796
print(data[n-1])

"""
흠... 이것도 답을 보게되었다. 하지만 이번에는 해설만 보고 풀어보았다.
감은 잡은 것 같다. 다음에는 더 쉽게 접근이 가능할 것 같다.
"""