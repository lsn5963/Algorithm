import itertools as it
n, f = map(int, input().split())
data = [1]*n

for i in range(1,n):
    data[i] = data[i-1] * (n-i) // i
a = list(range(1, n+1))

for tmp in it.permutations(a):
    sum=0
    for l,x in enumerate(tmp):
        sum += x*data[l]
    
    if sum == f:
        for x in tmp:
            print(x, end = " ")
        break