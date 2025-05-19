"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:

输入: numRows = 1
输出: [[1]]
 

提示:

1 <= numRows <= 30
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans  = [[1] * n for n in range(1,numRows+1)]
        if numRows <=2:
            return ans
        for i in range(2,numRows):
            for j in range(1,i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans