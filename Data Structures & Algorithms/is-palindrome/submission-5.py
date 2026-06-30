class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = "".join(char for char in s if char.isalnum()).lower()
        l, r = 0, len(alpha_s) - 1
        while l <= r:
            if alpha_s[l] == alpha_s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
        
