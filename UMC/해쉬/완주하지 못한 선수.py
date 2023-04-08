def solution(participant, completion):
    dt = {}
    cnt = 0
    for ptp in participant:
        if ptp in dt:
            dt[ptp] += 1
        else:
            dt[ptp] = 0
    for cpt in completion:
        dt[cpt] -= 1
    
    for i in dt:
        if dt[i] == 0:
            return i
    
    
    