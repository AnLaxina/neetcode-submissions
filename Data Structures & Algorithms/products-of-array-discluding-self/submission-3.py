class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        # prefix and postfix
        prefix = postfix = 1

        # multiply all the numbers before i
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        # multiply all numbers after i but start at the end and make my way down
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result