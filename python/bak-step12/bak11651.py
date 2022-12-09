#11651
#좌표 정렬하기 2

z=[]
for i in range(int(input())):
     z.append(list(map(int, input().split())))
z = sorted(z, key = lambda x : (x[1], x[0]))

for i in range(len(z)):
     print('{} {}'.format(z[i][0], z[i][1]))
