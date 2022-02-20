class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums)-1
        
        while left <= right:

            val = nums[left] + nums[right]

            if target == val:
                return [left + 1, right + 1]

            if val < target:
                left += 1

            else:
                right -= 1
        return
        
        
