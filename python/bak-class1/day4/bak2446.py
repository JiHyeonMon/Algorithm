#2446
#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

star = int(input())

for i in range(0, star):
    print("{}{}".format(' '*i,'*'*(star*2-i*2-1)))
for i in range(star-2,-1,-1):
    print("{}{}".format(' '*i,'*'*(star*2-1-i*2)))
