for i in range(1,11):
    n = int(input())
    data = list(map(int,input().split()))
    cnt = 0
    for j in range(2,n-2):
        for k in (j-2,j-1,j+1,j+2):
            if data[j] < data[k]:
                break
        else:
           cnt += data[j] - max(data[j-2],data[j-1],data[j+1],data[j+2])
    print("#", end="")
    print(i,end=" ")
    print(cnt)
