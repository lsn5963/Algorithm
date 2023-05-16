t = int(input())

data = [int(input()) for _ in range(t)]
cu = [25,10,5,1]

for da in data:
    for j in cu:
        print(da//j, end = " ")
        da = da%j
    print()
