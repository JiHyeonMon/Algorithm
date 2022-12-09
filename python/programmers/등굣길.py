def solution(m, n, puddles):
    d = [[0 for i in range(m+1)] for i in range(n+1)]
    d[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
                
            if [j, i] in puddles:
                d[i][j] = 0
                
            else:
                d[i][j] = (d[i-1][j]+d[i][j-1]) % (1000000007)

    return d[n][m]

'''
m   n   puddles   return
4   3   [[2, 2]]
'''
