"""
Given a binary tree, find the length of the longest consecutive sequence path.
The path refers to any sequence of nodes from some starting node 
to any node in the tree along the parent-child connections. 
The longest consecutive path need to be from parent to child (cannot be the reverse).
"""

#Solution 1: BFS with queue
from collections import deque
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res, queue = 0, deque([(root, 1)])
        while queue:
            node, length = queue.popleft()
            res = max(res, length)
            for kid in (node.left, node.right):
                if kid:
                    l = length + 1 if kid.val == node.val + 1 else 1
                    queue.append((kid, l))
        return res
 
 #Solution 2: DFS with stack
 class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res, stack = 0, [(root, 1)]
        while stack:
            node, length = stack.pop()
            res = max(res, length)
            for kid in (node.left, node.right):
                if kid:
                    l = length + 1 if kid.val == node.val + 1 else 1
                    stack.append((kid, l))
        return res
 #Solution 3: DFS recursive
 class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, parent, length):
            if not node: return length
            length = length + 1 if (parent and node.val== parent.val + 1) else 1
            return max(length, max(helper(node.left, node, length), helper(node.right, node, length)))
        return helper(root, None, 0)
 
 
