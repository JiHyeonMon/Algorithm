//
//  74. Search a 2D Matrix.swift
//  Algorithm
//
//  Created by 김지현 on 2022/12/10.
//

class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        
        var rowIndexInNumber = rowsCount - 1
        
        // matrix를 돌면서 어느 row에 속하는지 rowIndexInNumber에 저장
        //
        for (i, row) in matrix.enumerated() {

            guard let first = row.first else {
                return false
            }

            // row의 가장 작은 수보다 작은지 확인
            if target < first {
                rowIndexInNumber = i - 1
                break
            }
        }

        // [Exception] - matrix의 가장 작은 숫자보다 작은 target
        // matrix에 속하지 않는다.
        //
        if rowIndexInNumber < 0 {
            return false
        }
        
        // 이분 탐색 결과를 반환
        //
        return binarySearch(row: matrix[rowIndexInNumber], target: target)
    }

    func binarySearch(row: [Int], target: Int) -> Bool {

        // [Exception] 간단한 예외처리
        if row.count == 1 {
            guard let first = row.first else {
                return false
            }

            return first == target
        }

        // [Exception] 간단한 예외처리
        if row.count == 2 {
            guard let first = row.first, let last = row.last else {
                return false
            }

            return (first == target) || (last == target)
        }

        // 이분 탐색 위한 변수 설정
        //
        var left = 0
        var right = row.count - 1
        var pivot = (left + right) / 2

        // 이분 탐색
        //
        while (left <= pivot && pivot <= right) {

            // 값이 앞, pivot, 뒤 값이 target에 포함되면 true
            //
            if row[pivot] == target || row[left] == target || row[right] == target {
                return true
            }

            // [Exception]  [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13
            if right - left < 2 {
                return false
            }

            // pivot 재설정
            if row[pivot] < target {
                left = pivot
            } else {
                right = pivot
            }

            pivot = (left + right) / 2
        }

        return false
    }
}
