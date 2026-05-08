class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram = exact same characters as other string
        # Order can be different
        arr_s = sorted(s)
        arr_t = sorted(t)
        if arr_s == arr_t:
            return True
        return False