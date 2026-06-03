class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            s_count = {}
            t_count = {}

            for character in s:
                s_count[character] = 1 + s_count.get(character, 0)
            
            for character in t:
                t_count[character] = 1 + t_count.get(character, 0)
            
            return s_count == t_count