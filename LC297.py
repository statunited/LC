"""
Serialization is the process of converting a data structure or object 
into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later 
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string 
and this string can be deserialized to the original tree structure
"""

#Solution, recursive preorder
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if not node:
                res.append('Null')
            else:
                res.append(str(node.val))
                helper(node.left)
                helper(node.right)
        res = []
        helper(root)
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            val = next(vals)
            if val == 'Null':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        vals = iter(data.split())
        return helper()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
