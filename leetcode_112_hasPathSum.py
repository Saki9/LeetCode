class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    @title 112. 路径总和
    @method 深度优先搜索
    """

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.calculator(root, sum, 0)

    def calculator(self, root: TreeNode, sum: int, total: int) -> bool:
        if root == None or root.val == None:
            return False
        elif root.val + total == sum and root.left == None and root.right == None:
            return True
        else:
            return self.calculator(root.left, sum, total + root.val) or \
                   self.calculator(root.right, sum, total + root.val)


t = TreeNode(8)
t.left = TreeNode(9)
t.right = TreeNode(-6)
t.right.left = TreeNode(5)
t.right.right = TreeNode(9)
print(Solution().hasPathSum(t, 7))