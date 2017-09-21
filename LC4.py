"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Input: A1 with length m, A2 with length n, assuming m <= n.
Output: median of the combination of two arrays

Idea:
1. Find index i, j that divides the two arrays like the following:
    A1[0], ..., A1[i-1] | A1[i], ..., A1[m]
    A2[0], ..., A2[j-1] | A2[j], ..., A2[n]

2. 0 <= i <= m, and j = (m + n + 1)/2 - i

3. i and j will satisfy A1[i-1] <= A2[j] and A2[j-1] <= A1[i]

4. Such i, j will yield median of the combined array.

Algorithm:
1. iL = 0, iR = m 
2.  ##search for i, j
    ##bondary cases accounted
    i = (iL + iR)/2
    if (j == 0 or i == m or A1[i-1] <= A2[j]) and (i == 0 or j == n or A2[j-1] <= A1[j]):
        return i and j
    elif i > 0 and A1[i-1] > A2[j]:
        iR = i - 1
        repeat
    elif i < m and A2[j-1] > A1[i]:
        iL = i + 1
        repeat
3. ##find the median with i, j
    if m + n is odd:
        return max(A1[i-1], A2[j-1])
    else:
        return (max(A1[i-1], A2[j-1]) + min(A1[i], A2[j]))/2    
"""

#Solution
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        iL, iR, half_len = 0, m, (m + n + 1)/2
        while iL <= iR:
            i = (iL + iR)/2
            j = half_len - i
            if i > 0 and nums1[i-1] > nums2[j]:
                iR = i - 1
            elif i < m and nums2[j-1] > nums1[i]:
                iL = i + 1
            else:
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])
                if (m + n)%2 == 1:
                    return max_left
                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])
                return (max_left + min_right)/2.0
