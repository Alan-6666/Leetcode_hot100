"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：
对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
 
示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

示例 2：
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。

示例 3:
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
 

提示：

m == s.length
n == t.length
1 <= m, n <= 105
s 和 t 由英文字母组成
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        # 统计 t 中每个字符的出现次数
        t_count = Counter(t)
        required = len(t_count)

        # 左右指针和窗口内的统计
        l, r = 0, 0
        formed = 0
        window_counts = {}

        # 记录最小窗口的长度和起始位置
        min_len = float("inf")
        min_window_start = 0

        while r < len(s):
            # 将右指针指向的字符加入窗口
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # 如果当前字符的数量满足 t 中的要求，更新 formed
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            # 当窗口内的字符满足要求时，尝试收缩窗口
            while l <= r and formed == required:
                char = s[l]

                # 更新最小窗口
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window_start = l

                # 收缩窗口，移除左指针指向的字符
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1

                l += 1

            # 移动右指针
            r += 1

            # 如果没有找到符合条件的窗口，返回空字符串
        return "" if min_len == float("inf") else s[min_window_start:min_window_start + min_len]
    

                
s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s,t))
                
        