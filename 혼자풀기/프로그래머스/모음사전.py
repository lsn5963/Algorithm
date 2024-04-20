# from itertools import permutations
cnt, l = 0, {}


def solution(word):
    def dfs(s, n):
        global cnt
        global l
        if n > 5:
            return

        l[cnt] = s
        cnt += 1

        for i in range(5):
            dfs(s + ans[i], n + 1)

    ans = list("AEIOU")
    word = list(word)

    dfs("", 0)
    for idx, fd in l.items():
        if fd == "".join(word):
            return idx

