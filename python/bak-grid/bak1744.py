#1744
#수묶기

bigger1 = []
smaller0 = []
other = []

answer = 0
for i in range(int(input())):
     tmp = int(input())
     if tmp > 1:
          bigger1.append(tmp)
     elif tmp<0:
          smaller0.append(tmp)
     else:
          other.append(tmp)
bigger1.sort()
smaller0.sort()
while len(bigger1)>1:
     answer+= bigger1.pop() * bigger1.pop()
answer+=sum(bigger1)

while len(smaller0)>1:
     answer+=smaller0.pop(0)*smaller0.pop(0)

if len(smaller0)==1 and 0 in other:
     smaller0=[]
elif len(smaller0)==1:
     answer+=smaller0[0]

print(answer+sum(other))


