"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1：
输入：root = [1,2,3,null,5,null,4]
输出：[1,3,4]
解释：

示例 2：
输入：root = [1,2,3,4,null,null,null,5]
输出：[1,3,4,5]
解释：

示例 3：
输入：root = [1,null,3]
输出：[1,3]

示例 4：
输入：root = []
输出：[]

提示:
二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100 
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.pop(0)
                if i == n-1:
                    ans.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return ans
