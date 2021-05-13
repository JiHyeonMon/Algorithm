---
layout: post
title: "[프로그래머스] 압축"
date: 2021-05-03 23:59 +0530
categories: 프로그래머스, KAKAO
---

알고리즘 풀기 112일차

2018 KAKAO BLIND RECRUITMENT

:)

- # 압축

>

## < 문제 >

신입사원 어피치는 카카오톡으로 전송되는 메시지를 압축하여 전송 효율을 높이는 업무를 맡게 되었다. 메시지를 압축하더라도 전달되는 정보가 바뀌어서는 안 되므로, 압축 전의 정보를 완벽하게 복원 가능한 무손실 압축 알고리즘을 구현하기로 했다.

어피치는 여러 압축 알고리즘 중에서 성능이 좋고 구현이 간단한 LZW(Lempel–Ziv–Welch) 압축을 구현하기로 했다. LZW 압축은 1983년 발표된 알고리즘으로, 이미지 파일 포맷인 GIF 등 다양한 응용에서 사용되었다.

LZW 압축은 다음 과정을 거친다.

1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
5. 단계 2로 돌아간다.

압축 알고리즘이 영문 대문자만 처리한다고 할 때, 사전은 다음과 같이 초기화된다. 사전의 색인 번호는 정수값으로 주어지며, 1부터 시작한다고 하자.

색인 번호| 1 2 3 ... 24 25 26
단어| A B C ... X Y Z

예를 들어 입력으로 KAKAO가 들어온다고 하자.

1. 현재 사전에는 KAKAO의 첫 글자 K는 등록되어 있으나, 두 번째 글자까지인 KA는 없으므로, 첫 글자 K에 해당하는 색인 번호 11을 출력하고, 다음 글자인 A를 포함한 KA를 사전에 27 번째로 등록한다.
2. 두 번째 글자 A는 사전에 있으나, 세 번째 글자까지인 AK는 사전에 없으므로, A의 색인 번호 1을 출력하고, AK를 사전에 28 번째로 등록한다.
3. 세 번째 글자에서 시작하는 KA가 사전에 있으므로, KA에 해당하는 색인 번호 27을 출력하고, 다음 글자 O를 포함한 KAO를 29 번째로 등록한다.
4. 마지막으로 처리되지 않은 글자 O에 해당하는 색인 번호 15를 출력한다.

이 과정을 거쳐 다섯 글자의 문장 KAKAO가 4개의 색인 번호 [11, 1, 27, 15]로 압축된다.

## < 입력 >

입력으로 영문 대문자로만 이뤄진 문자열 msg가 주어진다. msg의 길이는 1 글자 이상, 1000 글자 이하이다.

## < 출력 >

주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력하라.

## < 풀이 >

```python

def solution(msg):
    dictionary={'A':1, 'B':2, 'C':3, 'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    answer = []

    while len(msg)>0:
        for i in range(len(msg), -1, -1):
            if msg[0:i] in dictionary.keys():
                answer.append(dictionary[msg[0:i]])

                dictionary[msg[0:i+1]] = list(dictionary.values())[-1]+1
                msg = str(msg[i:])
                break

    return answer

```

우선 알파벳을 딕셔너리에 각 번호로 저장한다.

그러고 입력으로 들어온 문자열이 있다면 계속 반복문을 진행.

우선 문자열 길이 제일 긴 것 부터 끝에서 하나 씩 줄여나가며 딕셔너리에 있는지 비교.

딕셔너리에 있다면 answer에 넣고 바로 뒷자리 문자까지 더해서 딕셔너리에 새로 추가한다.

그러고 해당 값 문자열에서 지운다.

>

아래는 다른 사람 풀이다.

```python

def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer

# 아스키 코드 이용 -> A = 65 -> 'A':1 저장

---

def solution(msg):
    myDic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,27)))
    answer = []

    state = 1 # 1: ok. 2: add
    while len(msg) > 0:
        temp = -1
        for j in range(1, len(msg)+1):
            if list(myDic.keys()).count(msg[0:j]) != 0:
                temp = myDic[msg[0:j]]
                state = 1
            else :
                # add to dictionary
                myDic[msg[0:j]] = len(myDic)+1
                state = 2
                break
        answer += [temp]
        if state == 2 :
            msg = msg[j-1:]
        else :
            msg = ""
    return answer

# python zip 함수 : zip() 은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다. -> A에 1 대응, B에 2 대응

```

딕셔너리 선언하는 부분이 굉장히 깔끔하다.
