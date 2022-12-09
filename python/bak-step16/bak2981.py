#2981
#검문

import math

N=int(input())
num_list=[]
while N>0:
     N-=1
     num_list.append(int(input()))
 
if num_list[0]<num_list[1]:
     m=num_list[1]-num_list[0]
else:
     m=num_list[0]-num_list[1]
    
m_candidate=[m]
for i in range(2,int(math.sqrt(m))+1):
     if m%i==0:
          m_candidate.append(i)
          m_candidate.append(m//i)
 
M=[]
for i in range(len(m_candidate)):
     r=num_list[0]%m_candidate[i]
     for j in range(1,len(num_list)):
          if r!=num_list[j]%m_candidate[i]:
               break
          if j==len(num_list)-1:
               M.append(m_candidate[i])
 
M.sort()
 
 
for k in M:
     print(k,end=' ')
