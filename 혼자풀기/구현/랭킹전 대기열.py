p, m = map(int, input().split())
people = []
for i in range(p):
    lv, id = input().split()
    people.append([int(lv), id])

rooms = []

for lv,nick in people:
    flag = False
    for i in range(len(rooms)):
        if len(rooms[i][1]) == m:
            continue
        if rooms[i][0] >= lv-10 and rooms[i][0] <= lv+10:
            flag = True
            rooms[i][1].append([lv,nick])
            break
    if flag == False:
        rooms.append([lv,[[lv,nick]]])
# print(rooms)
for room in rooms:
    room[1].sort(key = lambda x : x[1])
    if len(room[1]) != m:
        print("Waiting!")
        for j in room[1]:
            print(j[0], j[1])
    else:
        print("Started!")
        for j in room[1]:
            print(j[0],j[1])
