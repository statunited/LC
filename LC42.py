"""Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Key Idea:
    For each element, the water it can trap is equal to the minimum of maximum height of bars
    on both sides, minus its own height.
    water_trapped = min(max_height_of_left_bars, max_height_of_right_bars) - height_of_the_element
    
Solution 1: Brute Force
    For each of the element:
        loop over its left elements to find max left height
        loop over its right elements to find max right height
        calculate water trapped for the element

Solution 2: DP
    From left to right: find max left height for each element
    From right to left: find max right height for each element
    Loop over the elements to find water trapped

Solution 3: Using stack
    Use stack to keep track of the bars that are bounded by longer bars.
    loop over the array:
        while stack is not empty and height[current] > height[stack[-1]]:
            to_fill = stack.pop()
            dist = current - stack[-1] - 1
            bounded_height = min(height[current], height[stack[-1]]) - height[to_fill]
            ans += dist*bounded_height
        stack.append(current)
            
        if height[i] <= height[stack[-1]]: add i to stack
        else: stack.pop()
        
Solution 4: Two pointers
    L, R = 0, n-1
    while L < R:
        if height[L] < height[R]:
            if height[L] >= left_max: left_max = height[L]
            else: ans += left_max - height[L]
            L += 1
        else:
            if height[R] >= right_max: right_max = height[R]
            else: ans += right_max - height[R]
            R -= 1
"""

#Solution 1, Brute Force
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(height)):
            max_left = max(height[:i]) if i > 0 else 0
            max_right = max(height[i+1:]) if i < (len(height)-1) else 0
            water = min(max_left, max_right) - height[i]
            ans += max(0, water)
        return ans
        
 #Solution 2, DP
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        n = len(height)
        max_left, max_right = [0]*n, [0]*n
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        for i in range(n):
            water = min(max_left[i], max_right[i]) - height[i]
            ans += max(0, water)
        return ans
        
#Solution 3, Stack
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = current = 0
        stack = []
        for current in range(len(height)):
            while stack and height[current] > height[stack[-1]]:
                to_fill = stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1
                bounded_h = min(height[current], height[stack[-1]]) - height[to_fill]
                ans += distance*bounded_h
            stack.append(current)
        return ans
        
#Solution 4, two pointers
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans, left_max, right_max, L, R = 0, 0, 0, 0, len(height)-1
        while L < R:
            if height[L] < height[R]:
                if height[L] >= left_max: left_max = height[L]
                else: ans += left_max - height[L]
                L += 1
            else:
                if height[R] >= right_max: right_max = height[R]
                else: ans += right_max - height[R]
                R -= 1
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
