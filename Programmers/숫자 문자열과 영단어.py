def solution(s):
    alpha = ["zero","one","two","three","four",
    "five","six","seven","eight","nine"]

    dic_alpha = {"zero":0,"one":1,"two":2,"three":3,
    "four":4,"five":5,"six":6,"seven":7,
    "eight":8,"nine":9}

    sum = ""
    result = ""
    for i in s:
        if i>="a" and i<="z":
            sum += i
        else:
            sum += i
            result += i 
            sum = ""

        if sum in alpha:
            result += str(dic_alpha[sum])
            sum = "" 
    return int(result)
print(solution("one4seveneight"))