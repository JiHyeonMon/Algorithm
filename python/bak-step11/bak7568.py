#7568
#덩치

num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append([weight, height])

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")

    
'''
n = int(input())
w = []
h = []
answer = [0 for i in range(n)]
cnt = 1

for i in range(n):
     a, b = map(int, input().split())
     w.append(a)
     h.append(b)

while n>0:
     for i in range(n):
          if w[i] == max(w):
               if h[i] == max(h):
                    answer[i] = cnt
                    cnt+=1
                    w[i]=0
                    h[i]=0
               else:
                    answer[i] = cnt
                    w[i] = 0
               pass
     n-=1

print(answer)
'''
