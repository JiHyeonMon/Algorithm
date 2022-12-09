#11726
#2*n 타일링

n = int(input())
tile=[1,2]

if n>1:
     for i in range(2, n):
          tile.append((tile[i-1]+tile[i-2])%10007)
else:
     tile.pop()
print(tile[-1])
