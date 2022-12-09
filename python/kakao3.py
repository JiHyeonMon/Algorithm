from collections import deque
backup = []
def command(table, index, cmd):

    if cmd[0] == 'U':
        if index-int(cmd[2:])<0:
            index = 0
        else:
            index = index-int(cmd[2:])
        return table, index
    elif cmd [0] == 'D':
        if index+int(cmd[2:]) >= len(table):
            index = len(table)-1
        else:
            index = index+int(cmd[2:])
        return table, index
    elif cmd[0] == 'C':
        if index == len(table)-1:
            item = table.pop()
            backup.append([index, item])
            index = len(table)-1
        else:
            item = table.pop(index)
            backup.append([index, item])
        return table, index
    else:
        z = backup.pop()
        if z[0]<=index:
            index += 1
        table.insert(z[0], z[1])
        return table, index
        
def solution(n, k, cmd):
    answer = 'X'*n
    index = k
    table = [i for i in range(n)]
    for i in range(len(cmd)):
        table, index = command(table, index, cmd[i])
        
    for i in table:
        answer = answer[:i] +'O' + answer[i+1:]
    return answer

'''
n	k	cmd	result
8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	"OOOOXOOO"
8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]	"OOXOXOOO"
'''