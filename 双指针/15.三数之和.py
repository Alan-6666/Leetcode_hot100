"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
 

提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    def twoSum(self,nums, target):
        left = 0
        right = len(nums) -1
        ans = []
        while left < right:
            total_sum = nums[left] + nums[right]
            if  total_sum == target:
                ans.append([nums[left], nums[right], -target])
                while left < right and nums[left+1] == nums[left]:
                    left +=1
                while left < right and nums[right-1] == nums[right]:
                    right -=1
                left +=1
                right -=1

            elif total_sum > target:
                right -=1
            elif total_sum < target:
                left +=1
        return ans
        
    def threeSum(self, nums: [int]) -> [[int]]:
        ans = []
        #排序 + 双指针
        nums.sort()
        for i in range(0, len(nums)-2):
            #去重
            if i > 0 and nums[i]==nums[i-1]:
                continue
            two = self.twoSum(nums[i+1:], -nums[i])
            #添加到新的
            if two:
                ans.extend(two)
        return ans