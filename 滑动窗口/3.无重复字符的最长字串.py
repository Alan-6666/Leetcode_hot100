"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        counter = {}
        for i,c in enumerate(s):
            #记录字符出现次数
            if c not in counter.keys():
                counter[c]=1
            else:
                counter[c] +=1
            #如果出现重复字符，更新left指针，将第二个重复字符左侧的字符数置零
            #left更新到第二个重复的字符下标
            while counter[c] > 1:
                counter[s[left]]-=1
                left +=1
            #更新最长字串长度
            ans = max(ans, i - left + 1)
        return ans