def solution(board, moves):
    data = []
    count = 0
    for i in (moves):
        for j in range(len(board)):
            if board[j][i-1] != 0:
                data.append(board[j][i-1])
                board[j][i-1] = 0

                if len(data) > 1:
                    if data[-1] == data[-2]:
                        data.pop()
                        data.pop()
                        count += 2
                break
    return count


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

