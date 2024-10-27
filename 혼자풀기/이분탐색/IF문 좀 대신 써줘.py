import sys
n,m = map(int, sys.stdin.readline().rstrip().split())
chingho = [list(sys.stdin.readline().rstrip().split()) for _ in range(n)]
fights = [int(sys.stdin.readline().rstrip()) for _ in range(m)]

for fight in fights:
    lt, rt = 0, len(chingho)
    while lt<=rt:
        mid = (lt+rt)//2
        if fight <= int(chingho[mid][1]):
            rt = mid - 1
            rst = mid
        else:
            lt = mid + 1
        # print(rst)
    print(chingho[rst][0])