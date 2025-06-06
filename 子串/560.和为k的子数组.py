"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
 

提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = 0
        count = {} #记录前缀和的出现次数
        count[0] = 1 #当前和与目标值相等时，也为1
        ans = 0
        for n in nums:
            #类似前缀法
            presum +=n
            if presum - k in count.keys():
                ans +=count[presum - k]
            
            if presum not in count.keys():
                count[presum] = 1
            else:
                count[presum] += 1
        return ans
            

                
        