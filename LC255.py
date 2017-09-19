"""
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
You may assume each number in the sequence is unique.
Follow up:
Could you do it using only constant space complexity?
"""

#Solution1, O(n) space using stack
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low, stack = float('-inf'), []
        for num in preorder:
            if num < low:
                return False
            while stack and num > stack[-1]:
                low = stack.pop()
            stack.append(num)
        return True
        
        
#Solution2, O(1) space by using the array itself
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        #stack = preorder[:i]
        low, i = float('-inf'), 0
        for num in preorder:
            if num < low:
                return False
            while i and x > preorder[i-1]:
                low = preorder[i-1]
                i -= 1
            preorder[i] = num
            i += 1
        return True
