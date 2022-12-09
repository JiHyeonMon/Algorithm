#2869
#달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

a, b, v = map(int, input().split())

if (v-b)%(a-b)!=0:
     print((v-b)//(a-b)+1)
else:
     print((v-b)//(a-b))


'''
for answer in range(1, v):
     if (a-b)*(answer-1) + a >= v:
          print(answer)
          break
'''
