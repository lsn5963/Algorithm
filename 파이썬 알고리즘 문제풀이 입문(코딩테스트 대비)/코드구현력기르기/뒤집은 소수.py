n = int(input())

data = list(input().split())

def reverse(x):
    sum = ""
    for i in x:
            sum = i + sum
    return int(sum)

def isPrime(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    else:
        return True

for i in data:
    temp = reverse(i)
    
    if isPrime(temp):
        print(temp, end = " ")