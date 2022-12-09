#2941
#예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

alpha = ['c=','c-', 'dz=', 'd-','lj','nj', 's=', 'z=']

i = input()

for k in alpha:
    i = i.replace(k, '!')
        
print(len(i))
