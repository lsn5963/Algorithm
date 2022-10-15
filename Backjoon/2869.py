import sys
a,b,v = map(int, sys.stdin.readline().rstrip().split())

if (v-a) % (a-b) == 0:
    print((v-a) // (a-b)+1)
else:
    print((v-a) // (a-b)+2)

"""
수학적인 머리가 생각나지 않았다.
답을 보고 풀었지만 어려운 문제다.
"""