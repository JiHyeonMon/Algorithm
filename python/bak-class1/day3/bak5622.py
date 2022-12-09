#5622
#다이얼

def num_output(a):
    for i in range(0, len(num)):
        for j in range(0, len(num[i])):
            if num[i][j] in a:
                return num.index(num[i])
    
num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
sum = 0

for i in range(0, len(a)):
    sum += num_output(a[i])+3

print(sum)
