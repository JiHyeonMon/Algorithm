#10989
#수 정렬하기 3

'''
def merge_sort(n):
     v = len(n)
     if v<=1:
          return n
     v = v//2
     left = merge_sort(n[0:v])
     right = merge_sort(n[v:len(n)])
     
     return merge(left, right)

def merge(left, right):
     a=[]
     i, j = 0,0
     while (i<len(left) and j<len(right)):
          if left[i] < right[j]:
               a.append(left[i])
               i+=1
          elif left[i]>right[j]:
               a.append(right[j])
               j+=1
          else:
               a.append(left[i])
               a.append(right[j])
               i+=1;j+=1

     if i == len(left):
          a = a + right[j:len(right)]
     if j == len(right):
          a = a + left[i:len(left)]

     return a



n = [int(input()) for i in range(int(input()))]

answer = merge_sort(n)
print(*answer, sep="\n")
'''

import sys
n = int(input())
check_list = [0] * 10001

for i in range(n):
    a = int(sys.stdin.readline())
    check_list[a] = check_list[a] + 1

for j in range(len(check_list)):
    if check_list[j] !=0:
        for c in range(check_list[j]):
            print(j)


