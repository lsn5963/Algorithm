def solution(land):
    n = len(land)
    s = 0
    for i in range(1,n):
        for j in range(4):
            if j == 0:
                land[i][j] += max(land[i-1][j+1:])
            if j == 1:
                land[i][j] += max(land[i-1][0],land[i-1][2],land[i-1][3])
            if j == 2:
                land[i][j] += max(land[i-1][0],land[i-1][1],land[i-1][3])
            if j == 3:
                land[i][j] += max(land[i-1][0],land[i-1][1],land[i-1][2])
    return max(land[n-1])