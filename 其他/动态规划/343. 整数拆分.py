"""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。

 

示例 1:

输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
 

提示:

2 <= n <= 58
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], (i - j) * j, dp[i - j] * j)
        return dp[n]

"""
思路：
非线性dp

dp[i]表示数字i拆分成至少2个正整数的最大乘积

i 拆分2种可能，
1、j 和 i-j, 当i-j不能继续拆分，dp[i] = (i - j) * j
2、当i-j可以继续拆分，dp[i] = dp[i - j] * j

"""