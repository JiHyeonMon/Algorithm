#1110
#N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

num = int(input())

ten = num//10
one = num%10

cnt = 1

while True:
    try:
        new = (one*10)+(ten+one)%10
        if new==num:
            print(cnt)
            break
        else:
            ten = new//10
            one = new%10
            cnt+=1
    except:
        break

        
