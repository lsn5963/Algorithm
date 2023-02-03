def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)): 
        for j in range(len(arr2[0])): 
            for k in range(len(arr1[0])): 
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
    #         i[0] * arr2[0][0]
    #         i[1] * arr2[1][0]
    #         i[2] * arr2[2][0]

    #         i[0] * arr2[0][1]
    #         i[1] * arr2[1][1]
    #         i[2] * arr2[2][1]