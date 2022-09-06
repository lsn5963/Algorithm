import sys
data = sys.stdin.readline().rstrip()

data = data.split('-')

s = 0
for i in data[0].split('+'):
    s += int(i)

for i in data[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)


"""
이문제는 결국 못풀고 답을 봐버렸다. 좀만 더 생각을 했으면 풀었을 것 같은데
끈기가 부족했다.
"""