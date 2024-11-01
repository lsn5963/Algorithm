from collections import defaultdict
t = int(input())
for _ in range(t):
    w = input()
    k = int(input())

    minval, maxval = len(w)+1, -1
    alphabet_dict = defaultdict(list)
    for i in range(len(w)):
        alphabet_dict[w[i]].append(i)
    # print(alphabet_dict)
    for i in alphabet_dict.values():
        if len(i) < k:
            continue
        for j in range(len(i)-k+1):
            minval = min(minval, i[j+k-1]-i[j]+1)
            maxval = max(maxval, i[j+k-1]-i[j]+1)
    if maxval == -1:
        print(-1)
    else:
        print(minval,maxval)
