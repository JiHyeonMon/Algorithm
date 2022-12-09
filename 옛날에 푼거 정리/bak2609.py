#최대공약수와 최소공배수

def gcd (a, b) :
    while b!=0 :
        tmp = a % b
        a = b
        b = tmp
    return int(a)

def lcm (a, b, c):
    print(int(a*b/c))

a,b = map(int, input().split())

if a<b:
    tmp = a
    a=b
    b=tmp

print(gcd(a,b))
lcm(a,b, gcd(a,b))