"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        total = 0
        min_ = 0
        for n in nums:
            total +=n
            ans = max(ans, total - min_)
            min_ = min(min_, total)
        return ans

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp[i] 以 nums[i] 结尾的连续子数组的最大和
        nums[i] > 0: dp[i] = max(nums[i], dp[i-1] + nums[i])
        nums[i] <=0: dp[i] = max(nums[i],[dp[i-1] + nums[i])
        """
        n = len(nums)
        dp = [float("-inf")] * n
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))