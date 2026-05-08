class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store the num/value as a key, use the index as a value
        # Find the difference between the target and current num
        # If it exists in the hashmap, return the indices
        nums_map = dict()

        for index,value in enumerate(nums):
            difference = target - value
            if difference in nums_map:
                return [nums_map[difference], index]
            nums_map[value] = index
            
