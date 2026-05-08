class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # Assume that the array is NOT EMPTY and it only contains ints
        empty_dict = dict()
        for num in nums:
            if num not in empty_dict:
                empty_dict[num] = 1
            elif num in empty_dict:
                return True
        return False

         
