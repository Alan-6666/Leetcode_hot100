"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

 

示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2
 

提示:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
题目保证可以到达 nums[n-1]

"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        为了减少跳跃次数，需要每次在可跳范围内选择使下一个跳的更远的位置
        end: 当前达到的最远位置
        max_pos: 下一步能跳到的最远位置
        steps: 最少跳跃次数
        """
        end, max_pos = 0,0
        steps = 0
        #遍历到数组的倒数第二个位置时，跳跃次数已经确定，因为最后一个位置一定可以通过当前范围到达。
        #所以遍历到倒数第二个位置
        for i in range(len(nums)-1):
            #记录当前能走到的最大下标
            max_pos = max(max_pos, i + nums[i])
            #走到上一步的终点后，更新下一步的终点，步数+1
            if i == end:
                end = max_pos
                steps +=1
        return steps