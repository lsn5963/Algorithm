import sys
n = int(sys.stdin.readline().rstrip())

data = []
for _ in range(n):
    data = (sys.stdin.readline().rstrip())
    sum = 0

    for i in data:
        if i == '(':
            sum+=1
        else:
            sum -=1
        
        if sum< 0:
            break
    if sum == 0:
        print("YES")
    else:
        print("NO")

        
"""
이문제는 풀지 못하였다.
왜 스택이 필요한지 몰랐지만 sum이 결국 스택역할과 비슷한 것 같다.
"""