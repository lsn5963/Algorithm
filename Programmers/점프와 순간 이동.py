# def solution(n):
#     p = n
#     n = n//2
#     dp = [0] * (n+1)
#     if p == 1:
#         return 1
#     dp[1] = 1
    
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             dp[i] = dp[i//2]    
#         else:
#             dp[i] = dp[i//2]+1
#     if p % 2 == 0:
#         return dp[n]
#     else:
#         return dp[n] + 1
def solution(n):
    count = 1
    while n>2:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n-1
            count += 1
            
    return count
print(solution(1))
print(solution(1))