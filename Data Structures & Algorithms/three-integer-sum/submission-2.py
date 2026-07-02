class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            current_num = nums[i]

            if current_num > 0:
                break
            elif i > 0 and current_num == nums[i - 1]:
                continue
            
            L, R = i + 1, len(nums) - 1

            while L < R:
                total = current_num + nums[L] + nums[R]
                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    
                    result.append([current_num, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1

            
        return result