#2588
#(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

a = input()
b = input()
c = list(map(int, b))

print(int(a)*int(b[2]))
print(int(a)*int(b[1]))
print(int(a)*int(b[0]))
print(int(a)*int(b))
