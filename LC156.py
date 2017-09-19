"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling 
(a left node that shares the same parent node) or empty, 
flip it upside down and turn it into a tree 
where the original right nodes turned into left leaf nodes. Return the new root.
"""

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        def helper(node):
            if not node.left: return node
            curr, pre = node, node
            while curr.left:
                pre = curr
                curr = curr.left
            curr.left = pre.right
            pre.left, pre.right = None, None
            curr.right = helper(node)
            return curr
        return helper(root)
