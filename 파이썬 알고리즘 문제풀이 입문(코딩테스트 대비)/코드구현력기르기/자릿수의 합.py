n = input()
def digit_sum(x):
    result = []
    max = 0
    cnt = 0
    for idx, i in enumerate(x):
        s = sum(list(map(int,str(i))))
        if s > max:
            max = s
            cnt = idx
            
    return x[cnt]
data = list(map(int, input().split()))
print(digit_sum(data))