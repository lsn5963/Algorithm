def solution(s):
    data = []
    for i in s:
        if i == "(":
            data.append("(")
        else:
            if data == []:
                return False
            data.pop()
    if data == []:
        return True
    else:
        return False