'''
Find_Minimum_in_Rotated_Sorted_Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #find peak 
        left, right = 0, len(nums) - 1
        
        while left < right: 
            
            mid  = (left + right) // 2
            
            #if middle element is greater than the rightmost element, smallest element resides in the right
            if nums[mid] > nums[right]: 
                left = mid + 1
            else: #if middle element is smaller than rightmost element, we want to search in the left side of the middle element 
                right = mid
        
        minimum = left
        
        return(nums[minimum])
