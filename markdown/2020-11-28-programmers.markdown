---
layout: post
title:  "프로그래머스 코딩테스트 문제6"
date:   2020-11-28 04:00 +0530
categories: python
---

알고리즘 풀기 27일차

:)


- #모의 고사

수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

```python

math1=[1,2,3,4,5]
math2=[2,1,2,3,2,4,2,5]
math3=[3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    score = [0,0,0]
    answer=[]
    for i in range(len(answers)):
        if answers[i]==math1[i%5]:
            score[0]+=1
        if answers[i]==math2[i%8]:
            score[1]+=1
        if answers[i]==math3[i%10]:
            score[2]+=1
            
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    return answer

```

분류가 완전탐색 문제였다. 그러니 모든 경우를 다따져 점수를 매겨야겠다 싶었다. (사실 그거 외엔 떠오르지도 않았음)

세 명의 패턴이 다 다른데 일단 규칙이 있는 곳까지(서클 생기는 곳까지) 리스트로 만들었고, 입력이 100개 이렇게 들어올 수도 있으니 %나머지 연산으로 서클 내에서 리스트 값이 매칭되도록 했다.

세 명의 점수를 score리스트에 기록하고 answer리스트는 score리스트의 최댓값이 같은 사람을 넣어주는 것으로 마무리했다.

---

- #체육복

점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.


```python

def solution(n, lost, reserve):
    person = [1 for i in range(n)]
    for i in range(len(reserve)):
        person[reserve[i]-1]+=1
    for i in range(len(lost)):
        person[lost[i]-1]-=1
        
    for i in range(len(person)):
        if i == 0:
            if person[0]==2 and person[1]==0:
                person[0]=1
                person[1]=1
        elif i == len(person)-1:
            if person[i]==2 and person[i-1]==0:
                person[i]=1
                person[i-1]=1
        else:
            if person[i]==2:
                if person[i-1]==0:
                    person[i]=1
                    person[i-1]=1
                elif person[i+1]==0:
                    person[i]=1
                    person[i+1]=1
                    
    answer = n-person.count(0)
    return answer

```

탐욕법 문제. 보고 문제가 길면 겁을 먹게 돼 겁부터 생겼지만 풀다보니 어려운 문제는 아니었던거 같다. 
근데 앞뒤로 탐색을 하는 문제인데 너무 ㅋㅋㅋㅋㅋ 노가다 식으로 값을 바꿔준 것 같다. 

처음에 코드 돌렸을 때 33점이 나와서 뭐가 문젠가 싶었는데, 문제 조건을 제대로 안봐서 여분이 있으면 배열에 2, 잃어버리면 0을 넣었는데 처음에 다 1이다가 여분 있으면 +1, 잃어버림 -1로 바꾸니 됐다. 일단 전자가 안됐던 이유는 여분을 가져온 것을 도둑맞을 수도 있기 때문에 2라고 판단내릴 수 없다. 

---