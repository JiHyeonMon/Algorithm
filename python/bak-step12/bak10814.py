#10814
#나이순 정렬

l = []

for i in range(int(input())):
     l.append(input().split())

l = sorted(l, key = lambda x:int(x[0]))

for i in range(len(l)):
     print('{} {}'.format(l[i][0], l[i][1]))
