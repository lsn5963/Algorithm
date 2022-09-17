import sys
n = int(sys.stdin.readline().rstrip())
count = 0
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1)+ fib(n-2)
data = [0 for _ in range(41)]
def fibonacci(n):
    data[1] = 1
    data[2] = 1
    cnt = 0
    for i in range(3,n+1):
        cnt +=1
        data[i] = data[i-1] + data[i-2]
    return cnt
    

print (fib(n),fibonacci(n) )
"""
dp로 접근하면 count가 적다.
"""