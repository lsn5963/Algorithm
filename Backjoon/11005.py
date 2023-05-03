n, b = map(int, input().split())

data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rst = ""
while n != 0:
    rst = data[n % b] + rst
    n = n // b
print(rst)