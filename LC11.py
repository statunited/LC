"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Idea: 
Use two pointers, one starts at 0, one at n. Each time, moves the pointer at the position
with smaller ai towards the other pointer.
"""
#Solution
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R = 0, len(height)-1
        ans = 0
        while L < R:
            ans = max(ans, (R - L)*min(height[L], height[R]))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return ans
