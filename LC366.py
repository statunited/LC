"""
Given a binary tree, collect a tree's nodes as if you were doing this: 
Collect and remove all leaves, repeat until the tree is empty.
Example:
[1,2,3,4,5] --> [[4,5,3],[2],[1]]
"""
#Solution using bottom-up recursive approach
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if not node: return 0
        level = 1 + max(self.helper(node.left), self.helper(node.right))
        if not self.res or len(self.res) < level:
            self.res.append([node.val])
        else:
            self.res[level-1].append(node.val)
        return level
    

       
        
