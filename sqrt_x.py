class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        idea --> keep reducing the search space!!!: 
            explore integer space 0~x inclusive 
            if the middle number squared is equal to x, then return middle number 
            if the middle number squared is greater than x then truncate part after and including the middle number
                set right = mid 
            if the middle number square is less than x then truncate the part up to the middle number 
                set left = mid + 1
                
            repeat above until left <= right 
            
            return right - 1 or left - 1 
        '''
        
        if x == 0: 
            return 0
        
        left, right = 0, x
        
        while (left <= right): 
            
            mid = (left + right) // 2
            
            if mid**2 == x: 
                return mid 
            elif mid**2 > x: 
                right = mid - 1
            else: 
                left = mid + 1
                
        return left - 1
