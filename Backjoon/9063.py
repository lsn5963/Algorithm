n = int(input())
width = []
height = []
for i in range(n):
    a,b = map(int,input().split())
    width.append(a)
    height.append(b)

print((max(width)-min(width))*(max(height)-min(height)))
