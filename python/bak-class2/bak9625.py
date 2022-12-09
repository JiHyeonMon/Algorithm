#9625
#BABBA

num = int(input())
a=1
b=0

for i in range(num):
     tmp = b
     b+=a
     a=tmp
     

print(a, b)

'''
a->b
b->ba

1 0 a 
0 1 b
1 1 ba
1 2 bab
2 3 babba
3 5 babbabab
5 8 babbababbabba
'''
