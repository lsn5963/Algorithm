def solution(strings, n):
    strings.sort()
    strings.sort(key = lambda x: (x[n]))
       
    return strings

print(solution(["sun", "bed", "car"],1))
print(solution(["abce", "abcd", "cdx"],2))