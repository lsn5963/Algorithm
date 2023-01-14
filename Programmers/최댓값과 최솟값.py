def solution(s):
    a = max(list(map(int,s.split(" "))))
    b = min(list(map(int,s.split(" "))))
    sum = ""
    sum += str(b) + " " + str(a)
    return sum