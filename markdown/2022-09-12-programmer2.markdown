---
layout: post
title: "[프로그래머스] 올바른 괄호"
date: 2022-09-12
categories: 프로그래머스
level: 2

---



## < 문제 >

괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

## <제한사항>

- 문자열 s의 길이 : 100,000 이하의 자연수
- 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

## < 풀이 >

```python

// 정확도 통과, 효율성 불통
//
import Foundation

func solution(_ s:String) -> Bool
{
    
    if s.prefix(1) == ")" || s.suffix(1) == "(" || s.count % 2 == 1 {
        return false
    }
    
    var stack: [Character] = []
    
    for s in s {
        
        if s == ")" && stack.last == "(" {
            stack.popLast()
            continue
        }
        
        stack.append(s)
    }
    
    return stack.isEmpty
}

```

효율성에서 실패해서 stack아닌 Int로 세어서 비교하기로 수정


```python

import Foundation

func solution(_ s:String) -> Bool
{
    
    if s.prefix(1) == ")" || s.suffix(1) == "(" || s.count % 2 == 1 {
        return false
    }
    
    var count: Int64 = 0
    var prev: Character?
    
    for s in s {
        
        if s == ")" && count == 0 {
            return false
        }
        if s == ")", 
        let prev = prev, prev == "(" {
            count -= 1
            continue
        }
        
        count += 1
        prev = s
    }
    
    return count == 0
}

```
