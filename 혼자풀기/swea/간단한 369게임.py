from collections import defaultdict
n = 33
for i in range(1,n+1):
    d = defaultdict(int)
    i = str(i)
    for j in i:
        d[j] += 1
    # print(d)
    cnt = 0
    for k,num in d.items():
        if k == "3" or k == "6" or k == "9":
           cnt += num
    if cnt == 0:
        print(i, end = " ")
    else:
            print("-"*cnt, end = " ")
