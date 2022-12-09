#11650
#좌표 정렬하기

z=[]
for i in range(int(input())):
    z.append(list(map(int, input().split())))
z=sorted(z)
for i in range(len(z)):
     print('{} {}'.format(z[i][0], z[i][1]))
