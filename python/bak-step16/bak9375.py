#9375
#패션왕 신해빈

for i in range(int(input())):
     n = int(input())
     cloth={}
     answer = 1
     for i in range(n):
          name, kind = input().split()
          if kind not in cloth.keys():
               cloth[kind] = 1
          else:
               cloth[kind] += 1
     for kind in cloth:
          answer *= (cloth[kind]+1)
     print(answer-1)
