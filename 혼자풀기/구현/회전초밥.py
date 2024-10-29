n,d,k,c = map(int, input().split())
data = [int(input()) for _ in range(n)]*2
data = data[:n+k-1]
rst = 0
for i in range(n):
    tmp = data[i:i+k]
    tmp.append(c)
    # print(tmp)
    rst = max(len(set(tmp)), rst)
print(rst)