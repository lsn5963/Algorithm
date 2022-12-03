def solution(s, n):
    damun = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    somun = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    answer = ""
    for i in s:
        if i.isupper():
            temp = damun.index(i)
            answer += damun[(temp+n) %26]
        elif i.islower():
            temp = somun.index(i)
            answer += somun[(temp+n) %26]
        else:
            answer += ' '

    return answer
    

print(solution("AB",1))
print(solution("Z",1))
print(solution("a B z",4))