def solution(s):
    data = ["",0,0]
    count = 0
    for i in s:
        if data[0] == "":
            data[0] = i
            data[1] += 1
        elif data[0] == i:
            data[1] += 1
        else:
            data[2] += 1   
        
        if data[1] == data[2]:
            count += 1
            data = ["",0,0]
    if data != ["",0,0]:
        count += 1
    return count