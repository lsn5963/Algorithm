import sys
melon = int(sys.stdin.readline().rstrip())
data = []

for i in range(6):
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))

w = 0
w_index = 0
h = 0
h_index = 0

for i in range(6):
    if data[i][0] == 1 or data[i][0] == 2:
        if w < data[i][1]:
            w = data[i][1]
            w_index = i
    elif data[i][0] == 3 or data[i][0] == 4:
        if h < data[i][1]:
            h = data[i][1]
            h_index = i
# print(w,h,w_index,h_index)

mw = abs(data[(w_index - 1) % 6][1] - data[(w_index + 1) % 6][1])
mh = abs(data[(h_index - 1) % 6][1] - data[(h_index + 1) % 6][1])

print(((w*h)-(mw*mh))*melon)