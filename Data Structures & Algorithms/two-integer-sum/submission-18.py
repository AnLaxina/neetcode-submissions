class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for index, num in enumerate(nums):
            storage[num] = index
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in storage and storage[complement] != index:
                return [index, storage[complement]]
        
        return []
