import sys
n = int(sys.stdin.readline().rstrip())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline().rstrip()))
def isPrime(num):
    if n <2:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
temp = []
for i in data:
    # for j in range(1, i):
    #     if i%j == 0:
    #         print("소수아님")
    #         break

    a = i//2
    b = i//2
    while(a>0):

        if isPrime(a) and isPrime(b):
            print(a,b)
            break
        else:
            a -= 1
            b += 1


"""
무언가 어려운 문제인데 쉬운것 같다.
답을 안보고 푸는 실력이 되고싶다.
"""