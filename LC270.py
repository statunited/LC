"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""

#recursive
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.res = None
        def helper(node, target):
            if node:
                if self.res is None: 
                    self.res = node.val
                if abs(node.val - target) < abs(self.res - target):
                    self.res = node.val
                kid = node.left if target < node.val else node.right
                helper(kid, target)
        helper(root, target)
        return self.res
        
 #iterative
 class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = None
        curr = root
        while curr:
            if res is None or (abs(curr.val - target) < abs(res - target)):
                res = curr.val
            curr = curr.left if target < curr.val else curr.right
        return res
