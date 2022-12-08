# a, b = map(int, input().strip().split(' '))
# sum = ['*' * a for i in range(b)] 
# for i in sum:
#     print(i)

a, b = map(int, input().strip().split(' '))
sum = ''
for i in range(b):
    for j in range(a):
        sum += '*'
    sum += '\n'

print(sum)
