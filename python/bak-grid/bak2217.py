#2217
#로브

n = int(input())
rope = []
value=[]
for i in range(n):
     rope.append(int(input()))
rope.sort(reverse = True)

for i in range(n):
     value.append(rope[i]*(i+1))

     
print(max(value))
