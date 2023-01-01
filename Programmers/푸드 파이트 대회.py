def solution(food):
    first = ""
    last = ""
    for i in range(1,len(food)):    
        f = food[i] 
        while f > 1 :
            first += str(i)
            last = str(i) + last
            f -= 2
    return first + "0" + last