def solution(s):
    
    sum = ""
    temp = 0
    for i in s:
        if i ==" ":
            temp = 1
            sum += i
        elif temp ==1 and i>="a" and i<="z":
            sum += i.upper()
            temp = 0
        elif temp == 0 and i >="A" and i<="Z":
            sum += i.lower()
        elif temp ==1 and i >="A" and i<="Z":
            temp = 0
            sum += i
        else:
            temp = 0
            sum += i
    if sum[0] >="a" and sum[0] <="z":
        sum = sum[0].upper() + sum[1:]
    return sum
    # s = s.split(" ")
    # for i in range(len(s)):
    #     s[i] = s[i][:1].upper() + s[i][1:].lower()
    #     print(s[i])
    # return ' '.join(s)
print(solution("   3people   unFollowed me"))
# print(solution("     "))
# print(solution("3pople 3ldld 3PPPPZZ"))