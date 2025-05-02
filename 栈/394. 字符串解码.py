"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

提示：

1 <= s.length <= 30
s 由小写英文字母、数字和方括号 '[]' 组成
s 保证是一个 有效 的输入。
s 中所有整数的取值范围为 [1, 300] 
"""

class Solution:
    def decodeString(self, s: str) -> str:
        st1 = [] #已解码字符串
        st2 = [] #左括号前数字
        num = 0
        res = "" 
        for c in s:
            if  c.isdigit():
                num = num * 10 + int(c) 
            elif c == "[":
                st1.append(res) #记录当前已解码字符串
                st2.append(num) #记录当前数字
                res = "" #重置，为了获取待解码的字符串
                num = 0
            elif c == "]":
                cur_res = st1.pop()
                cur_num = st2.pop()
                res = cur_res + res * cur_num #上一个已解码字符串 + 当前字符串 * 当前数字
            else: 
                res +=c
        return res
                
