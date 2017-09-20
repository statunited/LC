"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes 
from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example:
[1,2,3] => 6
"""

#Solution, bottom-up recursive
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        def helper(node):
            if not node: return 0
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            self.res = max(self.res, node.val + left + right)
            return node.val + max(left, right)
        helper(root)
        return self.res
