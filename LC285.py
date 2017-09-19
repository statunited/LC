"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
Note: If the given node has no in-order successor in the tree, return null.
"""
#recursive not using BST
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.count = 0
        self.res = None
        def helper(node):
            if not node: return
            helper(node.left)
            if self.count == 1:
                self.res = node
                self.count = 0
            if node == p:
                self.count = 1
            helper(node.right)
        helper(root)
        return self.res
        
#iterative using BST
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        res = None
        curr = root
        while curr:
            if curr.val <= p.val:
                curr = curr.right
            elif curr.val > p.val:
                res = curr
                curr = curr.left
        return res
