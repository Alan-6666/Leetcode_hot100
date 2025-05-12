"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        dp[i][j] = min(dp[i][j-1],dp[i-1][j])
        dp[0][0] = grid[0][0]
        dp[0][1] = grid[0]1] + dp[0][0]
        dp[1][0] = grid[1][0] + dp[0][0]

        """

        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]

        #初始化第一行
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        #初始化第一列
        for j in range(1,len(grid)):
            dp[j][0] = dp[j-1][0] + grid[j][0]

        for i in range(1, len(grid)):
            for j in range(1,len(grid[0])):
                #当前最小值等于上、左的最小值 + 当前数值
                dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j]
        
        return dp[-1][-1]
    
"""
grid = [[1,2],[5,6],[1,1]]
输出
8
"""
print(Solution().minPathSum([[1,2],[5,6],[1,1]]))