import sys

x = int(sys.stdin.readline().rstrip())

end = 0
line = 0
while x > end:
    line+=1
    end += line
diff = end - x 
if line % 2 ==0:
    n = line - diff
    m = diff + 1
else:
    n = diff + 1
    m = line - diff

print(f'{n}/{m}')

"""
답을 보고 풀었다.
패턴찾기가 어려웠다.
"""
