class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted(s)
        list_t = sorted(t)
        if list_s == list_t:
            return True
        return False