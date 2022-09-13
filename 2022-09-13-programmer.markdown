---
layout: post
title: "[프로그래머스] 숫자의 표현"
date: 2022-09-13 09:01
categories: 프로그래머스

---



## < 문제 >

Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15

4 + 5 + 6 = 15

7 + 8 = 15

15 = 15

자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

## <제한사항>

- n은 10,000 이하의 자연수 입니다.

## < 풀이 >

```python

def solution(n):
    
    // n == n 무조건 하나는 충족
    // 이후 조건에서는 (연속된 수니까) 절반 부터 시작
    answer = 1
    
    // 순차 덧셈 시작할 숫자
    startNum = 1
    
    while startNum < n/2:
    
        // 합을 저장해둘 변수
        result = 0
        
        // 시작 넘버부터 순차대로 n까지 더해본다.
        for i in range(startNum, n):
            result += i
            
            // 순차로 더하다가 n 보다 커지면 실패
            if result > n:
                startNum += 1
                break
                
            // n이 되면 충족
            if result == n:
                answer += 1
                startNum += 1
                break
                
    return answer

```

swift로만 이제 푸는데, 해당 문제는 swift 지원을 안해서 오랜만에 (원래 오랜만에 푸는 알고리즘이지만) python으로 풀어봤다.


