#2751
#수 정렬하기 2


def merge_sort(v):
     if len(v)<=1:
          return v
     m = len(v)//2
     left = merge_sort(v[0:m])
     right = merge_sort(v[m:len(v)])

     return merge(left, right)
     
def merge(left, right):
     v=[]
     i, j = 0,0
     while (i<len(left) and j<len(right)):
          if left[i] <= right[j]:
               v.append(left[i])
               i+=1
          else:
               v.append(right[j])
               j+=1

     if i == len(left):
          v += right[j:len(right)]
     if j == len(right):
          v += left[i:len(left)]

     return v

v = [int(input()) for i in range(int(input()))]
m = merge_sort(v)

print(*m, sep="\n")
