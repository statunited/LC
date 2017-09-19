"""
Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.
"""
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        def helper(node):
            if not node: return True
            left = helper(node.left)
            right = helper(node.right)
            if left and right:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
                self.count += 1
                return True
            return False
        helper(root)
        return self.count
