#13301
#타일 장식물

n = int(input())
tile = [1,1]
for i in range(2, n):
     tile.append(tile[i-1]+tile[i-2])
     
if n == 1:
     print(4)
elif n == 2:
     print(6)
else:
     print((tile[n-1] + tile[n-2]*2 + tile[n-3]) *2 )
