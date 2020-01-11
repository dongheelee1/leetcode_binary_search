class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        idea: 
            evaluate mid index and see if the middle element is the target 
            
            if middle element is the target 
                return the mid index 
            if middle element is smaller than the target 
                adjust the left index to be mid + 1
            if middle element is greater than the target
                adjust the right index to be mid - 1
            keep doing above until right index and left index match 
            
            if the element at the current (left or right) index is the target: 
                then return that index 
            else: 
                target doesn't exist so return 1 
                
        '''
        left = 0 
        right = len(nums)-1 
        
        while(left < right): 
            
            mid = (left + right)//2 
            
            if nums[mid] == target: 
                return mid 
            elif nums[mid] < target: 
                left = mid + 1
            elif nums[mid] > target: 
                right = mid - 1
                
        if nums[left] == target: 
            return left
        return -1 
                
