n = int(input())
sum = 0 # 동전의 개수를 의미한다.

for num in 500,100,50,10:
    sum += n // num
    n = n % num

print(sum)
