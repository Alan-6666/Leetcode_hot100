"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
 

提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[[i][j] word1 前[i] 个字符串变成word[2] 前j个字符串的最少操作次数
        1、word1[i-1] == word[j-1] : dp[[i][j] = dp[[i-1][j-1] 
        2、word1[i-1] != word[j-1]: 
        dp[i][j] = min(do[i-1][j], d[i][j-1], dp[i-1][j-1]) +1
        #分别代表 在word1[i-1] 插入元素、在word[i-1]删除元素 、替换元素
        """
        size1, size2 = len(word1), len(word2)
        dp = [[0]* (size2 + 1) for _ in range(size1 + 1)]
        #初始化
        #1、都没有字符时，无需操作
        #2、word2为 0 时，插入i次
        #3、word1为 0 时，插入[j]次
        for i in range(1,size1 + 1):
            dp[i][0] = i
        for j in range(1,size2 + 1):
            dp[0][j] = j

        for i in range(1,size1 + 1):
            for j in range(1,size2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] 
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
        
        return dp[size1][size2]