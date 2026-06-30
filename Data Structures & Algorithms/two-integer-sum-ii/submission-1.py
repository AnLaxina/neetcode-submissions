class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            current_sum = numbers[L] + numbers[R]
            if  current_sum == target:
                return [L + 1, R + 1]
            elif current_sum > target:
                R -= 1
            elif current_sum < target:
                L += 1
        
        return []