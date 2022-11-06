import sys
n,k = map(int, sys.stdin.readline().rstrip().split())

a = list(map(int, sys.stdin.readline().rstrip().split()))
ans = []
def merge_sort(a):
    if len(a) == 1:
        return a

    mid = (len(a)+1)//2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    i,j = 0,0
    a2 = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a2.append(left[i])
            ans.append(left[i])
            i +=1
        else:
            a2.append(right[j])
            ans.append(right[j])
            j +=1
    while i < len(left):
        a2.append(left[i])
        ans.append(left[i])
        i+=1
    while j < len(right):
        a2.append(right[j])
        ans.append(right[j])
        j+=1

    return a2
merge_sort(a)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)

        
