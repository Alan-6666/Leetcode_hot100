"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left is None and right is None:
                return True
            elif left is None and right:
                return False
            elif left and right is None:
                return False
            elif left.val != right.val:
                return False
            else:
                return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)