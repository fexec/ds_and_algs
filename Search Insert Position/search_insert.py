# https://leetcode.com/problems/search-insert-position/submissions/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1
        
        mid = 0
        
        while start <= end:
            
            mid = start + (end - start) // 2
            
            if  nums[mid] == target:
                
                return mid
            
            else:
      
                if nums[mid] < target:
                
                    start = mid + 1
                
                else:

                    end = mid - 1
                    
        
        if nums[mid] < target:
            
            return mid + 1
        
        else:
            return mid
