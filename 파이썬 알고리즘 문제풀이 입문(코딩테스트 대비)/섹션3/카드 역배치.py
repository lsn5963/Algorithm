data = list(range(1,21))

for _ in range(10):
    a,b = map(int,input().split())

    for i in range((b-a+1)//2):
        temp = data[a-1+i]
        data[a-1+i] = data[b-1-i]
        data[b-1-i] = temp

for i in data:
    print(i, end = " ")
