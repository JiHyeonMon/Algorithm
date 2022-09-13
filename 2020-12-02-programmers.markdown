---
layout: post
title:  "프로그래머스 코딩테스트 문제10"
date:   2020-12-02 03:45 +0530
categories: python
---

알고리즘 풀기 31일차

:)


- #스킬트리

선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

```python

def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)

    for i in range(len(skill_trees)):
        tmp = []
        f = True
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill_list:
                tmp.append(skill_trees[i][j])
            
        for k in range(len(tmp)):
            if tmp[k] != skill_list[k]:
                f = False
                break
        
        if f: answer+=1
    return answer

```

이거 풀고 감격의 눈물 흘릴 뻔,, 하 정말 한시간동안 생각했는데 다 하나씩 예외가 존재한 것.

우선 처음엔 skill이 있으면 index를 tmp변수에 넣어서 skill을 0->1->2 이렇게 순서대로 배우되 tmp보다 작다면 false로 하여 불가능이다 이렇게 코드를 짰다.
문제는 제일 첫번째 skill이 없어도 성립한다. 1->2->3 이렇게 0이 없어도 순차적 커지니까 성립.

그외 한두가지 더 시행착오를 겪었는데 기억도 안난다....하아,,

결론적으로 생각한 거는 이제 skill이 있다면 tmp리스트에 차곡차곡 넣고 해당 tmp리스트랑 skill의 순서가 같은지 보는 코드를 짰다.
skill이 0->1->2->3인데, 0->1->2까지 skill_trees에 있어도 성립하는 것이라서 tmp길이만큼만 테스트한다. (있는 만큼만, 순차면 됨.)

아무튼 바로 생각못해낸 게 ,,, 참 경험의 차이인지 생각의 차이인지,,, 공부를 한다고 이런 아이디어가 바로 떠오를 진 모르겠다. 그래도 풀어낸 내 스스로 칭찬 - ㅋㅋㅋㅋㅋㅋ

---



- #주식가격

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.


```python

def solution(prices):
    answer = []
    init = len(prices)
    i = 0
    while i<init:
            
        if prices[0] is min(prices):
            answer.append(len(prices)-1)
            prices.pop(0) 
        else:
            for j in range(1, len(prices)):
                if prices[0]>prices[j]:
                    answer.append(j)
                    prices.pop(0)
                    break
        i+=1
            
    return answer

```

어제 푼 주식가격 다시 풀어본 것이다. 

정확성 테스트는 다 맞는데 효율성 테스트가 다 시간초과다. ^^,,,하아,,,,

---


2단계 오고 더 이상 여긴 내 영역이 아닌거 같다 생각했는데, 해낸 뿌듯함. ^^ (그치만 어려워서 조만간 백준으로 돌아갈 것 같다..)

