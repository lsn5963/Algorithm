n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = len(a) - 1
last = 0
res = ""
tmp = []

while lt<=rt:
    # print(lt,rt)
    # print(tmp)
    # print(last)
    # if a[lt]>a[rt]:
    #     if a[rt] > last:
    #         tmp.append("R")
    #         last = a[rt]
    #         rt -= 1
    #     else:
    #         break
    # if a[lt]<a[rt]:
    #     if a[lt] > last:
    #         tmp.append("L")
    #         last = a[lt]
    #         lt += 1
    #     else:
    #         break

    # if last < a[lt] and last < a[rt]:
    #     if a[lt] > a[rt]:
    #         tmp.append("R")
    #         last = a[rt]
    #         rt -= 1
    #     if a[lt] < a[rt]
    #         tmp.append("L")
    #         last = a[lt]
    #         lt += 1

    tmp = []
    if a[lt] > last:
        tmp.append((a[lt],"L"))
    if a[rt] > last:
        tmp.append((a[rt], "R"))

    if tmp == []:
        break
    tmp.sort()

    if tmp[0][1] == "L":
        lt += 1
        res += "L"
    else:
        rt -= 1
        res += "R"
    last = tmp[0][0]
print(len(res))
print(res)
