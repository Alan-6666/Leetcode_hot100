"""
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        #查找最后一列，确定行
        left, right = 0, m-1
        #二分查找
        while left <= right:
            mid = left + (right - left) //2
            if matrix[mid][n-1] > target:
                right = mid -1
            elif matrix[mid][n-1] < target:
                left = mid +1
            else:
                return True
        #如果没有找到，left指向行数，left >=m,说明没找到符合范围的行
        if left >= m:
            return False
        row = left
        #遍历row的行
        left, right = 0, n -1
        #二分查找
        while left <= right:
            mid = left + (right - left) //2
            if matrix[row][mid] > target:
                right = mid -1
            elif matrix[row][mid] < target:
                left = mid +1
            else:
                return True
        return False
