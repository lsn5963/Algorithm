def solution(new_id):
    new_id = new_id.lower() #1
    sum = ""

    for i in new_id: #2
        if i>="a" and i<="z" or i>="0" and i<="9" or i == "-" or i =="_" or i == ".":
            sum += i
    
    count = 0
    s = ""

    for i in sum: #3
        if i == '.':
            count += 1
        else:
            count = 0
        
        if count >= 2:
            continue
        else:
            s += i
    
    if s[0] == ".": #4
        s = s[1:]
    if len(s) >= 1:
        if s[-1] == ".":
            s = s[:-1]

    if s == "": #5
        s +="a"

    if len(s) >= 16: #6
        s = s[:15]
        if s[-1] == ".":
            s = s[:-1]

    if len(s) <= 2:
        while len(s) != 3:
            s += s[-1]
    return s

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))