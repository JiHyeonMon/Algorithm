#1018
#체스판 다시 칠하기

whiteBoard = [
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    ]

blackBoard = [
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    ]

    
def isChess(c):
     cnt = 0
     if c[0][0]=="W":
          for i in range(8):
               for j in range(8):
                    if c[i][j]!= whiteBoard[i][j]:
                         cnt+=1
     else:
          for i in range(8):
               for j in range(8):
                    if c[i][j]!= blackBoard[i][j]:
                         cnt+=1
     return cnt

h, w = map(int, input().split())
chess=[]
check=[]
answer=[]
n = h+w-16
for i in range(h):
     chess.append(input())

for i in range(h-7):
     check=[]
     for j in range(w-7):
          check=[]
          for k in range(8):
               check.append(chess[i:i+8][k][j:j+8])
          answer.append(isChess(check))

print(min(answer))
