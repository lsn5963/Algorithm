def func(n):
    if n >0:
        func(n//2)
        print(n%2, end = "")
n = int(input())

func(n)