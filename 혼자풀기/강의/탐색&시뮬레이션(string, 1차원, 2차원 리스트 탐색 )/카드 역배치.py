card = list(range(1,21))
data = [list(map(int,input().split())) for _ in range(10)]


for a,b in data:
    tmp = card[a-1:b]
    tmp = tmp[::-1]
    # print(tmp)
    card[a-1:b] = tmp
    # print(card)

for i in range(20):
    print(card[i], end= " ")