"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

 

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
 

提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        定长滑动窗口
        """
        n = len(s)
        n_p = len(p)
        ans = []
        target = {}
        counter = {}
        #获取目标词以及数量, 以及统计字串的key
        for sub_s in  p:
            if sub_s not in target.keys():
                target[sub_s] =1
                counter[sub_s] = 0
            else:
                target[sub_s] +=1


        left , right = 0, 0
        while right < n:
            if s[right] in counter.keys():
                counter[s[right]] +=1
            
            if counter == target:
                ans.append(left)
            #当right 大于等于target长度时，移动窗口
            if right >= n_p -1:
                if s[left] in target.keys():
                    counter[s[left]] -=1
                left +=1        
            right +=1
        return ans
    
    
s = "cbaebabacd"

p = "abc"
print(Solution().findAnagrams(s, p ))