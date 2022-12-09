#1193
#X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.


num = int(input())
i = 1
j = 1
while num-1>1:
    #오른쪽 한칸
    j+=1
    num-=1
    #왼쪽 대각선
    for j in range(j, 1, -1):
        if(num==1):
            break
        i+=1
        j-=1
        num-=1
    #아래쪽 한 칸
    i+=1
    num-=1
    #오른쪽 대각선
    for i in range(i, 1, -1):
        if(num==1):
            break
        i-=1
        j+=1
        num-=1

print("{}/{}".format(i,j))
        
    
