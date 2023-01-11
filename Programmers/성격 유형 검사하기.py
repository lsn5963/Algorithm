def solution(survey, choices):
    alpha = {"R":0,
            "T":0,
            "C":0,
            "F":0,
            "J":0,
            "M":0,
            "A":0,
            "N":0}
    
    data = {1:3,
           2:2,
           3:1,
           4:0,
           5:1,
           6:2,
           7:3}
    count = 0
    for i in survey:
        first = i[0]
        second = i[1]
        
        if choices[count] > 4:
            alpha[second] += data[choices[count]]
        elif choices[count] < 4:
            alpha[first] += data[choices[count]]
        
        count += 1
        
    sum = ""
    
    if alpha["R"] >= alpha["T"]:
        sum += "R"
    elif alpha["R"] < alpha["T"]:
        sum += "T"
        
    if alpha["C"] >= alpha["F"]:
        sum += "C"
    elif alpha["C"] < alpha["F"]:
        sum += "F"
    
    if alpha["J"] >= alpha["M"]:
        sum += "J"
    elif alpha["J"] < alpha["M"]:
        sum += "M"
    
    if alpha["A"] >= alpha["N"]:
        sum += "A"
    elif alpha["A"] < alpha["N"]:
        sum += "N"
        
    return sum