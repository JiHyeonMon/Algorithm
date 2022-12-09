---
layout: post
title: "[프로그래머스] 이진 변환 반복하기"
date: 2022-09-12
categories: 프로그래머스
level: 2

---



## < 문제 >

0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.

x의 모든 0을 제거합니다.
x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.

0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.

## <제한사항>

- s의 길이는 1 이상 150,000 이하입니다.
- s에는 '1'이 최소 하나 이상 포함되어 있습니다.

## < 풀이 >

```python

import Foundation

func solution(_ s:String) -> [Int] {
    
    var s = s
    
    // 이진 변환의 횟수
    var sequence: Int = 0
    var removedZero: Int = 0
    
    while true {
        let zero_count = s.filter {$0 == "0"}.count
        removedZero +=  zero_count
        sequence += 1
        
        if s.count - zero_count == 1 {
            break
        }
        
        s = changeBinary(length: s.count - zero_count)
    }

    return [sequence, removedZero]
}

func changeBinary(length: Int) -> String {
    
    var num = length
    var result = ""
    var stack: [Int] = []
    
    repeat {
        let reminder = num%2
        stack.append(reminder)
        num = num / 2
    } while (num > 0)
    
    for i in stack.reversed() {
        result += String(i)
    }
    
    return result
}

```
