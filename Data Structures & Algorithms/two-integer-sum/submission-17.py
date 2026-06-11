class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for index, value in enumerate(nums):
            nums_dict[value] = index
        
        for index, value in enumerate(nums):
            complement = target - value
        
            if complement in nums_dict and index != nums_dict[complement]:
                return [index, nums_dict[complement]]
        
        return []