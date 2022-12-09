def solution(board, moves):
    blanket=[]
    answer = 0
    for k in range(0, len(moves)):
        for i in range(0, len(board)):
            if board[i][moves[k]-1] != 0:
                if blanket and blanket[-1] == board[i][moves[k]-1]:
                    answer += 1
                    blanket.pop()
                else:
                    blanket.append(board[i][moves[k]-1])
                board[i][moves[k]-1] = 0
                break
    return answer*2 #터진 인형은 두배! 두개씩 터지니까

'''
    top = blanket[-1]
    for j in range(len(blanket)-2, 0, -1):
        if(top == blanket[j]):
            answer += 1
            top = blanket[j]
        else:
            top = blanket[j]
'''
    

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))

