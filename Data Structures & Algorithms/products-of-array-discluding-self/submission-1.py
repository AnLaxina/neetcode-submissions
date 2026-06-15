class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            current_index = i
            current_product = 1
            for index, num in enumerate(nums):
                if index != current_index:
                    current_product *= num
            result.append(current_product)
        
        return result
                