class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         set_duplicates = set()
         for num in nums:
            if num not in set_duplicates:
                set_duplicates.add(num)
            elif num in set_duplicates:
                return True
         return False
