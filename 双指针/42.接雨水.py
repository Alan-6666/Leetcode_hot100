"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        单调栈解决
        1、当前大于等于栈顶，出栈，计算雨水量。否则进栈
        """
        ans = 0
        stack = [] #记录下标
        n = len(height)
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                
                cur = stack.pop()
                #当左侧存在时，才可能接到雨水
                if stack:
                    left = stack[-1]
                    right = i
                    width = right - left -1 
                    high = min(height[i], height[stack[-1]]) - height[cur] #注意cur是下标
                    ans += width * high
            
            stack.append(i) #注意cur是下标
        return ans