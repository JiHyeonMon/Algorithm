---
layout: post
title: "[프로그래머스] 프렌즈 4블록"
date: 2021-05-04 23:59 +0530
categories: 프로그래머스 KAKAO
---

알고리즘 풀기 113일차

2018 KAKAO BLIND RECRUITMENT

:)

- # 프렌즈 4블록

>

## < 문제 >

블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".

같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

![image](https://user-images.githubusercontent.com/50662636/117006285-320b6400-ad23-11eb-81e6-534a469c6ea8.png)

만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다.

같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.

![image](https://user-images.githubusercontent.com/50662636/117006298-36d01800-ad23-11eb-8b1a-b54060073531.png)

블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.

![image](https://user-images.githubusercontent.com/50662636/117006315-3afc3580-ad23-11eb-8370-7c2a85caab43.png)

만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.

![image](https://user-images.githubusercontent.com/50662636/117006327-3df72600-ad23-11eb-8ce4-e3e3f995902c.png)

위 초기 배치를 문자로 표시하면 아래와 같다.

    TTTANT
    RRFACC
    RRRFCC
    TRRRAA
    TTMMMF
    TMMTTJ

각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

## < 입력 >

입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.

> 2 ≦ n, m ≦ 30

board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.

## < 풀이 >

```python

def solution(m, n, board):
    answer = 0
    turn = [[_ for i in range(m)] for _ in range(n)]

    # board 돌리기 - 시계방향 90도 - 리스트에서 빼면 앞으로 밀어넣기 가능하게
    for i in range(n):
        for j in range(m):
            turn[i][j] = board[m-j-1][i]

    while True:
        # temp라는 임시 리스트 - 여기에 팡!터지는 리스트의 index만 넣는다.
        # 반복문 돌며 2*2 터지는 문자 있어도 바로 없애면 겹쳐서 터질 블록이 안터지기에 temp에 인덱스 넣어두고 팡!터질 블록 검사 다 하고 삭제 들어간다.
        temp = []

        # 2*2씩 검사 시작
        for i in range(n-1):
            for j in range(m-1):
                # 4칸이 같은 수인지 확인하고 0이 아닌지 확인한다. (0은 빈칸이므로 제외)
                if turn[i][j] == turn[i][j+1] == turn[i+1][j] == turn[i+1][j+1] and turn[i][j]!=0:
                    # set으로 중복 없애기 위해 list안에 tuple 형태로 넣음
                    temp.append((i, j))
                    temp.append((i+1, j))
                    temp.append((i, j+1))
                    temp.append((i+1, j+1))

        # 2*2가 겹치는 칸일 경우 index 두번 들어간다. set을 이용해서 중복은 제외한다.
        temp = sorted(set(temp))

        # while문 나올 조건 - 검사 다 했는데도 2*2 같은 값 없는 경우
        if not temp:
            break

        # 중복 없앤 temp값 == 이번에 터질 블록 수
        answer += len(temp)

        # temp에 있는 index 값들 블록 제거 들어간다.
        # list의 pop, remove, del 모두 하나씩 밖에 안지워짐.
        # 근데 하나 지울 경우 index가 다 밀리기 때문에 일단 해당 칸 ''으로 세팅하고 이 다음에 빈칸 없애주는 작업 추가 진행
        for i in temp:
            turn[i[0]][i[1]] = ''

        # 이제 보드판에서 빈칸인 칸은 없애며 다시 보드판 그린다.
        # 블록이 빠지면서 나머지 칸은 0으로 세팅해준다.
        for i in range(len(turn)):
            turn[i] = [v for v in turn[i] if v]
            if len(turn[i])<m:
                for j in range(len(turn[i]), m):
                    turn[i].append(0)

    return answer

```

풀이는 따로 적는 것보다 코드위에 적어두는게 나중에 봐도 이해가 잘 될 거 같아 주석으로 달았다.

["CCBDE", "AAADE", "AAABF", "CCBBF"]

입력으로 위와 같은 board가 들어온다면, 왼쪽 리스트인데 이를 오른쪽처럼 돌려주는 작업을 거친다.

    CCBDE           CAAC
    AAADE           CAAC
    AAABF   -->     BAAB
    CCBBF           BBDD
                    FFEE

터지는 퍼즐은 2\*2 정사각형이라 블록을 돌린다고 바뀌지 않는다. 이렇게 돌리면 블록 검사 후 터진 블록 뺄 때 앞으로 밀어주면 된다.

python의 zip함수를 써서 리스트를 쉽게 돌릴 수 있는 거 같은데 tuple의 형태로 return 되어 나중에 이용이 힘들어 새로운 리스트를 만들어 값을 채워줬다.

각 턴이 돌 때마다, 터질 블록 체크 --> 터질 블록 인덱스 저장 --> 체크 완료 후 블록 터트리기 --> 빈칸 채우기 (반복)
