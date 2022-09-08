import sys
n = int(sys.stdin.readline().rstrip())

st = []
for _ in range(n):
    st.append(sys.stdin.readline().rstrip().split())
data= []
for i in range(n):

    if st[i][0] == 'push':
        data.append(st[i][1])
    elif st[i][0] == 'pop':
        try:
            print(data.pop())
        except:
            print(-1)
    elif st[i][0] == 'size':
        print(len(data))
    elif st[i][0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif st[i][0] == 'top':
        try:
            print(data[-1])
        except:
            print(-1)

"""
이문제는 쉽게 풀었다.
하지만 정답을 보고나니 try except를 사용하지 않아도 풀 수 있었다. 
또한 입력을 따로 받았는데 그럴 필요가 없다.

input() 참고 https://codingexplore.tistory.com/18
"""