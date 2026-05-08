class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = dict()
        for index, num in enumerate(nums):
            difference = target - num
            if difference in my_map:
                return [my_map[difference], index]
            else:
                my_map[num] = index
