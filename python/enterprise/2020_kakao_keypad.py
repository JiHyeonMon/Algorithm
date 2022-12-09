#2020 카카오 인턴십
#키패드 누르기

def solution(numbers, hand):
    L = [1,4,7,'*']
    M = [2,5,8,0]
    R = [3,6,9,'#']
    answer = ''
    l_now = '*'
    r_now = '#'
    RL_dif = []

    for i in range(0, len(numbers)):

        if numbers[i] in L:
            answer+='L'
            l_now = numbers[i]
        elif numbers[i] in R:
            answer+='R'
            r_now = numbers[i]
        else:
            if r_now in M:
                RL_dif.append(abs(M.index(r_now)-M.index(numbers[i])))
            else:
                RL_dif.append(abs(R.index(r_now)-M.index(numbers[i]))+1)
                
            if l_now in M:
                RL_dif.append(abs(M.index(l_now)-M.index(numbers[i])))
            else:
                RL_dif.append(abs(L.index(l_now)-M.index(numbers[i]))+1)
            
            if RL_dif[0]==RL_dif[1]:
                if hand == 'right':
                    answer+='R'
                    r_now=numbers[i]
                else:
                    answer+='L'
                    l_now=numbers[i]
            else:
                if RL_dif[0]<RL_dif[1]:
                    answer+='R'
                    r_now=numbers[i]
                else:
                    answer+='L'
                    l_now=numbers[i]
            RL_dif=[]
    return answer
