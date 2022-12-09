#1003
#피보나츠

def fib(k):
     fib_zero=[1,0]
     fib_one=[0,1]
     for i in range(2, k+1):
          fib_zero.append(fib_zero[i-2]+fib_zero[i-1])
          fib_one.append(fib_one[i-2]+fib_one[i-1])
     return "{} {}".format(fib_zero[k], fib_one[k])
          
for i in range(int(input())):
     n = int(input())
     print(fib(n))
