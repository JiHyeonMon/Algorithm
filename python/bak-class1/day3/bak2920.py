#2920
#연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

a = list(map(int, input().split()))
p =""

if a[0] == 1 :
    for i in range(0, 8):
        if a[i] != i+1:
            p = "mixed"
            break
        else:
            p = "ascending"
elif a[0] == 8:
    for i in range(0, 8):
        if a[i] != 8-i:
            p = "mixed"
            break
        else:
            p= "descending"
else:
    p = "mixed"

print(p)


'''
l = list(map(int, input().split()))
asc = [i for i in range(1, 9)]
dsc = [i for i in range(8, 0, -1)]

if l == asc:
    print("ascending")
elif l == dsc:
    print("descending")
else:
    print("mixed")
'''
