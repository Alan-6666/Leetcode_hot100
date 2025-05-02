"""
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。

输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
示例 2：

输入：root = [1,2]
输出：1

提示：

树中节点数目在范围 [1, 104] 内
-100 <= Node.val <= 100
"""

from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)  #左子树高度
            right = dfs(root.right) #右子树高度
            
            nonlocal ans
            ans = max(ans,(left + right)) #更新最大直径
            return max(left, right ) + 1 #返回当前节点的高度
        dfs(root)
        return ans
