"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

 
示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0
 
提示：
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        完全背包问题，通过加入一层for循环转化为 0-1背包问题
        """
        size = len(coins)
        #初始化
        dp = [[float("inf")] * (amount + 1) for _ in range(size + 1)]
        #当目标位0时，硬币数量也为0
        #当硬币数为0时，目标不为0时，dp[0][j] 为float
        for i in range(size +1):
            dp[i][0] = 0
        
        for i in range(1,size + 1):
            for j in range(1, amount + 1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j - coins[i-1]] + 1 )
        if dp[size][amount] == float("inf"):
            return -1
        else:
            return dp[size][amount]