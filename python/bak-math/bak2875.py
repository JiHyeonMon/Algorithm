#2875
#대회 or 인턴


girl, boy, k = map(int, input().split())
team = 0
while girl+boy>=k+3 and girl >= 2 and boy >= 1:
     team+=1
     girl-=2
     boy-=1

print(team) 
