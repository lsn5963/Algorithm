n = list(input())

width = ["a","b","c","d","e","f","g","h"]
height = [1,2,3,4,5,6,7,8]

move = [[-1,-2],[1,-2],[-2,1],[-2,-1],[2,1],[2,-1],[-1,2],[1,2]] 
wn = width.index(n[0])
hn = height.index(int(n[1]))

cnt = 0

for mv in move:
    if wn + mv[0] < 0 or hn + mv[1] < 0 or wn + mv[0] > 7 or hn + mv[1] > 7:
        continue
    else:
        cnt += 1

print(cnt)