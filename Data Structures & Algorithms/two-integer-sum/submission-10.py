class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for index, current_num in enumerate(nums):
            tracker[current_num] = index
        
        for index, current_num in enumerate(nums):
            diff = target - current_num

            if diff in tracker and tracker[diff] != index:
                return [index, tracker[diff]]
        return []