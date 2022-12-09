def check(i, j, place):
    # 상
    if i>0 and place[i-1][j] == 'P' :
        return False
    if i>1 and place[i-2][j] == 'P' and place[i-1][j] != 'X':
        return False
    # 하
    if i<4 and place[i+1][j] == 'P':
        return False
    if i<3 and place[i+2][j] == 'P' and place[i+1][j] != 'X' :
        return False
    # 좌
    if j>0 and place[i][j-1] == 'P':
        return False
    if j>1 and place[i][j-2] == 'P' and place[i][j-1] != 'X':
        return False
    # 우
    if j<4 and place[i][j+1] == 'P' :
        return False
    if j<3 and place[i][j+2] == 'P' and place[i][j+1] != 'X':
        return False

    # 좌상
    if i>0 and j>0 and place[i-1][j-1] == 'P' and (place[i][j-1]!='X' or place[i-1][j]!='X'):
        return False
    # 좌하
    if i<4 and j>0 and place[i+1][j-1] == 'P' and (place[i][j-1] != 'X' or place[i+1][j] != 'X'):
        return False
    # 우상
    if i>0 and j<4 and place[i-1][j+1] == 'P' and (place[i][j+1]!='X' or place[i-1][j]!='X'):
        return False
    # 우하
    if i<4 and j<4 and place[i+1][j+1] == 'P' and (place[i][j+1]!='X' or place[i+1][j]!='X'): 
        return False
    return True

def solution(places):
    answer = []
    for place in places:
        answer.append(1)
        TF = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not check(i, j, place):
                        TF = False
                        break
            if not TF:
                answer[-1] = 0
                break
                        
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])