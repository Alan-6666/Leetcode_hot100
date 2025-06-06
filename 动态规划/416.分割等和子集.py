"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        0-1背包问题
        物品 是nums
        weight value 是 sum(nums) //2
        """
        total = sum(nums) 
        if total % 2 !=0:
            return False
        
        target = total //2

        dp = [ [0] *  (target + 1) for i in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            for j in range(target +1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - nums[i-1]] + nums[i-1])

        if dp[-1][-1] == target :
            return True
        else:
            return False 