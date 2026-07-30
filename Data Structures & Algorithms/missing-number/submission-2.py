class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        if 0 not in nums:
            return 0
        if n not in nums:
            return n    
        else:
            for i in range(len(nums)-1):
                if nums[i]+1 != nums[i+1]:
                    return nums[i]+1    
        