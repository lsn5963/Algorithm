import sys

n = int(sys.stdin.readline().rstrip())

def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    hanoi_tower(n-1, start, 6-start-end)

    print(start, end)

    hanoi_tower(n-1, 6-start-end, end)


print(2**n -1)

hanoi_tower(n, 1, 3)

"""
하노이는 유명한 재귀문제이다.
답을 보고풀었지만 다시봐야겠다.
"""