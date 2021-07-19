---
layout: post
title: "[프로그래머스] 숫자 문자열과 영단어"
date: 2021-07-19 23:01
categories: 프로그래머스 2021카카오
---

알고리즘 풀기 231일차

:)

- # 숫자 문자열과 영단어

## < 문제 >

네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

  1478 → "one4seveneight"

  234567 → "23four5six7"

  10203 → "1zerotwozero3"

이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.


## < 풀이 >

```python

numberStringList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def solution(s):
    answer = ""
    tmp = ""
    for num in s:
        if num.isdigit():
            answer+= str(int(num))
        else:
            tmp += num
            if tmp in numberStringList:
                answer+=str(numberStringList.index(tmp))
                tmp = ""
    return int(answer)

```

분명 푼 문제 같은 느낌은 해당 코딩테스트에서 풀었던 문제겠죠?

쉽게쉽게 다시 풀었습니다.

string형태의 숫자를 먼저 배열로 넣어두고, 해당 string을 int로 넣어야함에 배열 index를 넣어주게 했습니다. 

python 의 isdigit() 함수를 사용해서 true일 경우 해당 값을 string으로 넣고, 아닐 경우 문자로 된 숫자이기에 tmp 에 잠시 넣어놨다 tmp가 문자로 된 숫자로 완성되면 해당 index를 string으로 answer에 넣습니다. 

answer에 string을 넣는 이유는 int결과값을 더해주면 정말 수식 더하기가 되기에 string으로 변환해 숫자들을 넣고 integer형으로 결과 값을 반환해줍니다. 

