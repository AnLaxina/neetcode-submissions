class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in set_nums:
                # num would be start of sequence
                length = 0
                while (length + num) in set_nums:
                    length += 1
                longest = max(longest, length)
        
        return longest