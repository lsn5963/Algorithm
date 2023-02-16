n = int(input())
data = list(map(int, input().split()))
lt = 0
rt = len(data)-1
last = 0
sum = ""
while lt <= rt:
    if last < data[lt] and last < data[rt]:
        if data[lt] > data[rt]:
            last = data[rt]
            rt -= 1
            sum += "R"
        elif data[lt] < data[rt]:
            last = data[lt]
            lt += 1
            sum += "L"
    elif last < data[lt] and last > data[rt]:
        last = data[lt]
        lt += 1
        sum += "L"
    elif last > data[lt] and last < data[rt]:
        last = data[rt]
        rt -= 1
        sum += "R"
    else:
        break

print(len(sum))
print(sum)