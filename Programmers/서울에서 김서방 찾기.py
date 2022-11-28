def solution(seoul):
    for i in range(0,1000):
        if seoul[i] == "Kim":
            return "김서방은 "+str(i)+"에 있다"

print(solution(["Jane", "Kim"]))