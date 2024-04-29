rst = 0


def solution(k, dungeons):
    n = len(dungeons)
    check = [0] * (n + 1)
    visited = [False] * (n + 1)

    def dfs(l, np, cnt):
        global rst
        rst = max(cnt, rst)
        for i in range(n):
            if visited[i] == False:
                if dungeons[i][0] <= np:
                    visited[i] = True
                    dfs(l + 1, np - dungeons[i][1], cnt + 1)
                    visited[i] = False

    dfs(0, k, 0)
    return rst