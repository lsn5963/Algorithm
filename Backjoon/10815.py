import sys

n = int(sys.stdin.readline().rstrip())
odata = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
cdata = list(map(int, sys.stdin.readline().rstrip().split()))
odata.sort()
for i in cdata:
    low, high = 0, n-1

    while low <= high:
        mid = (low+high) // 2
        if odata[mid] > i:
            high = mid - 1
        elif odata[mid] < i:
            low = mid + 1
        elif odata[mid] == i:
            print(1, end = " ")
            break

    if low > high:
        print(0, end = " ")
