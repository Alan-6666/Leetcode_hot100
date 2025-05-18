"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
示例 2:

输入: preorder = [-1], inorder = [-1]
输出: [-1]
 
提示:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均 无重复 元素
inorder 均出现在 preorder
preorder 保证 为二叉树的前序遍历序列
inorder 保证 为二叉树的中序遍历序列

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def createTree(preorder, inorder, n):
            if n == 0:
                return None
            k = 0
            #根据前序遍历第一个元素，找到其在中序遍历的位置
            while preorder[0] != inorder[k]:
                k +=1
            node = TreeNode(inorder[k])
            #分成左、右两个子树
            node.left  = createTree(preorder[1:k+1], inorder[0:k], k)
            node.right = createTree(preorder[k+1:],inorder[k+1:], n - k -1)
            return node
        return createTree(preorder,inorder, len(inorder))