def solution(n, start, end, roads, traps):
    answer = []
    k = 0
    while True:
        if start == end:
            answer.append(k)
        can = []
        for i in range(len(roads)):
            if roads[i][0] == start:
                can.append(roads[i][1])
        print(can)  
        for i in range(len(can)):
            k += roads[start][i][2]
            start = can[i]
            if start in trap:
                for j in range(len(roads)):
                    roads[j] = [roads[j][1], roads[j][0], roads[j][2]]
            
    return answer

'''
n	start	end	roads	traps	result
3	1	3	[[1, 2, 2], [3, 2, 3]]	[2]	5
4	1	4	[[1, 2, 1], [3, 2, 1], [2, 4, 1]]	[2, 3]	4
'''