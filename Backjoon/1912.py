import sys

n = int(sys.stdin.readline().rstrip())

p = list(map(int, sys.stdin.readline().rstrip().split()))


dp = [0] *(n+1)
dp[0] = p[0]
for i in range(1, n):
    dp[i] = max(p[i], dp[i-1]+p[i])
print(max(dp))

"""
시간초과가 계속 나서 답지를 보고 풀었다.
생각해내기는 어려웠지만 자꾸 접근하면 나아질 것 같다.
"""