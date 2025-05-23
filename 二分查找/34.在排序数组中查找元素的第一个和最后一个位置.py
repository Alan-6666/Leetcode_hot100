"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        while left <=right:
            mid = left + (right - left)//2
            mid_nums = nums[mid]
            if mid_nums > target:
                right = mid - 1
            elif mid_nums < target:
                left = mid + 1
            else:
                #找到目标后，搜索左右两边是否存在相同数
                left = mid
                right = mid
                while left -1 >=0 and nums[left -1] == target:
                    left = left -1

                while right +1 < n and nums[right +1 ] == target:
                    right = right + 1

                return [left, right]
    
        return [-1, -1]