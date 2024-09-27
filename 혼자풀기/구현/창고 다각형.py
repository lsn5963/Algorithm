n = int(input())
datas = [list(map(int,input().split())) for _ in range(n)]
datas.sort()
# print(datas)
m = 0
for i in range(len(datas)):
    if m < datas[i][1]:
        m = datas[i][1]
        idx = i
        land = datas[i][0]

lt = 0
rt = n-1
ls = 0
prevl = datas[0][0]
prevs = datas[0][1]
for i in range(idx+1):
    if datas[i][1] >= prevs:
        ls += (datas[i][0] - prevl)*prevs
        prevs = datas[i][1]
        prevl = datas[i][0]
prevs = datas[-1][1]
prevl = datas[-1][0]
# print(ls)
for i in range(n-1,idx-1,-1):
    # print(i)
    if datas[i][1] >= prevs:
        ls += (prevl-datas[i][0])*prevs
        prevs = datas[i][1]
        prevl = datas[i][0]
print(ls+datas[idx][1])

# n = int(input())
#
# lst = []
# result = 0
# for i in range(n) :
#     a,b = map(int,input().split())
#     lst.append([a,b])
# #기둥을 x축 순으로 정렬한다.
# lst.sort()
#
# #가장 높은 기둥의 번호를 알아낸다.
# i = 0
# for l in lst :
#     if l[1] >result :
#         result = l[1]
#         idx = i
#     i += 1
#
# #초기 높이는 첫번째 기둥의 높이
# height = lst[0][1]
#
# #최대 높이전까지 돌면서 다음 기둥이 현재보다 높으면
# #result에 현재의 면적을 계산해서 더해주고 높이를 다음 기둥으로 갱신한다.
# for i in range(idx) :
#     if height < lst[i+1][1] :
#         result += height * (lst[i+1][0]-lst[i][0])
#         height = lst[i+1][1]
#     #아니면 그냥 현재면적을 더해준다.
#     else :
#         result += height * (lst[i+1][0] - lst[i][0])
#
# #뒤에서부터도 똑같이 진행한다.
# height = lst[-1][1]
#
# for i in range(n-1, idx, -1) :
#     if height < lst[i-1][1] :
#         result += height * (lst[i][0]-lst[i-1][0])
#         height = lst[i-1][1]
#     else :
#         result += height * (lst[i][0] - lst[i-1][0])
#
# print(result)