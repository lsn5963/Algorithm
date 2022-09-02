n = int(input())
count = 0

for k in range(n+1):
    # if k % 10 == 3 :
    #     count += 1
    # if k // 10 == 3 :
    #     count += 1
    for i in range(0,60):
        if k % 10 == 3 : # 03시 13시 ... 이런 부분은 모든 경우의 수인 3600번을 자동으로 count 해준다
            count += 3600
            break
        for j in range(0, 60):
            if i % 10 == 3 or i // 10 == 3:
                count += 60 # 03분 13분 ... 이런 부부은 모든 경우의 수인 60번을 자동으로 count 해준다.
                break
            if j % 10 == 3 or j // 10 == 3:
                count += 1
print(count)

"""
countt = 0
for i in range(n+1):
    for j in range (60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k) :
                countt+=1

print(countt)
"""

"""
이문제는 오류가 너무 나서 시간을 엄청썼다. 
그래서 답을 봤는데 너무 파이썬 식?으로 풀어서 당황했고 내가 너무 어렵게 생각한거라서 허무했다
그래서 끝까지 수학적으로 풀어내긴 했다. 
다음에는 문제가 너무 복잡하다면 이런 파이썬 식을 적극활용해야겠다.
"""

