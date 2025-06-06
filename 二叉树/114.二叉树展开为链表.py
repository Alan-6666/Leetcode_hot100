"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
 

示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [0]
输出：[0]
 
提示：
树中结点数在范围 [0, 2000] 内
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        要求链表顺序与前序遍历相同
        1、前序遍历
        2、变成链表
        """
        if root is None:
            return []
        queue = []
        def dfs(root, queue):
            if root is None:
                return 
            queue.append(root)
            dfs(root.left,queue)
            dfs(root.right,queue)
        dfs(root, queue)

        head = queue.pop(0)
        head.left = None
        while queue:
            temp = queue.pop(0)
            temp.left = None
            head.right = temp
            head = temp