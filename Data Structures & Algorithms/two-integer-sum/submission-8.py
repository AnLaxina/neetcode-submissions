class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # go through each num in nums
        # find the remainder via target - current num
        # in a map use the value as a key, and the index as the value
        
        my_map = {}

        for index, num in enumerate(nums):
            my_map[num] = index

        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in my_map and my_map[remainder] != index:
                return [index, my_map[remainder]]
        return []
