import sys

def get_stars(n):
    matrix = []

    for i in range(len(n)*3):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)

    return matrix

resultStar = ["***", "* *", "***"]

n = int(sys.stdin.readline().rstrip())
count = 0

while n != 3:
    n //= 3
    count += 1

for _ in range(count):
    resultStar = get_stars(resultStar)

for j in resultStar:
    print(j)

"""
어렵다.. 어렵다..
답을 보고했지만 어렵다..
"""