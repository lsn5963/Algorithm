n = int(input())
word = []
for _ in range(n):
    num = input().split()
    # print(num,len(num))

    flag = False
    for i in range(len(num)):
        if num[i][0].upper() not in word:
            word.append(num[i][0].upper())
            num[i] = "["+num[i][0]+"]"+num[i][1:]
            print(' '.join(num))
            flag = True
            break

    if not flag:
        for i in range(len(num)):
            check = False
            for j in range(len(num[i])):
                if num[i][j].upper() not in word:
                    word.append(num[i][j].upper())
                    num[i] = num[i][:j]+"["+num[i][j]+"]"+num[i][j+1:]
                    print(' '.join(num))
                    flag = True
                    check = True
                    break
            if check == True:
                break
    if not flag:
        print(' '.join(num))