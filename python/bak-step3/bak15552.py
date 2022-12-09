#15552
#각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

import sys

input = int(sys.stdin.readline())

for i in range(0, input):
    a, b = sys.stdin.readline().split()
    print(int(a)+int(b))
