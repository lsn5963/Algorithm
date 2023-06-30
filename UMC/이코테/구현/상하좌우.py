n = int(input())
data = list(map(str,input().split()))
tmp = [1,1]
x,y = 1,1
for dt in data:
    if dt == "L":
        tmp[1] -= 1
    elif dt == "R":
        tmp[1] += 1
    elif dt == "U":
        tmp[0] -= 1
    else:
        tmp[0] += 1

    if tmp[0] == 0 or tmp[1] == 0 or tmp[0] == n+1 or tmp[y] == n+1 :
        if dt == "L":
            tmp[1] += 1
        elif dt == "R":
            tmp[1] -= 1
        elif dt == "U":
            tmp[0] += 1
        else:
            tmp[0] -= 1

    # if dt == "L":
    #     ny = y - 1
    # elif dt == "R":
    #     ny = y - 1
    # elif dt == "U":
    #     nx = x - 1
    # else:
    #     nx = x + 1

    # if nx == 0 or ny == 0:
    #     continue
    # else:
    #     x,y = nx, ny


print(x,y)
    


    


print(tmp)