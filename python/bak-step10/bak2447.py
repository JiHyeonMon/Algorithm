#2447
#별찍기 - 10
'''
def star(s, n, k):
     sf = [[],[],[]]

     if k>n:
          return sf
     
     sf[0] = s*k
     
     for i in range(0, len(sf[0]) ):
          if i%2==0:
               sf[1].append(s*len(s))
          else:
               sf[1].append(" "*len(s))
     sf[2] = sf[0]

     k *= 3
     s= ''.join(sf[0])+''.join(sf[1])+''.join(sf[2])
     star(s, n, k)

n = int(input())
s = "*"

print(star(s, n, 3))
'''

def stars(n):
    s=[]
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            s.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            s.append(n[i % len(n)] * 3)
    return(list(s))

star = ["***","* *","***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1
    
for i in range(k):
    star = stars(star)
for i in star:
    print(i)


'''
def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]
 
def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' '*n]*n)
 
    return a + b + a
 
print('\n'.join(star10(int(input()))))
'''
