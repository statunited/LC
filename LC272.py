"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""

#Solution using hints
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        ret = []
        succ = []
        pred = []
        self.initializePredecessorStack(root, target, pred)
        self.initializeSuccessorStack(root, target, succ)
        if succ and pred and succ[-1].val == pred[-1].val:
            self.getNextPredecessor(pred)

        while k > 0:
            if not succ:
                ret.append(self.getNextPredecessor(pred))
            elif not pred:
                ret.append(self.getNextSuccessor(succ))
            else:
                succ_diff = abs(succ[-1].val - target)
                pred_diff = abs(pred[-1].val - target)
                if succ_diff < pred_diff :
                    ret.append(self.getNextSuccessor(succ));
                else:
                    ret.append(self.getNextPredecessor(pred));
            k -= 1
        return ret
    
    def initializeSuccessorStack(self, root, target, succ):
        while root:
            if root.val == target:
                succ.append(root)
                break
            elif root.val > target:
                succ.append(root)
                root = root.left
            else:
                root = root.right

    def initializePredecessorStack(self, root, target, pred):
        while root: 
            if root.val == target:
                pred.append(root)
                break
            elif root.val < target:
                pred.append(root)
                root = root.right
            else:
                root = root.left
                
    def getNextSuccessor(self, succ):
        curr = succ.pop()
        ret = curr.val
        curr = curr.right
        while curr:
            succ.append(curr)
            curr = curr.left
        return ret

    def getNextPredecessor(self, pred):
        curr = pred.pop()
        ret = curr.val
        curr = curr.left
        while curr:
            pred.append(curr)
            curr = curr.right
        return ret
