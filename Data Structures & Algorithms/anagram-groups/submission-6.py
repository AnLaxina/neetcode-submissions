from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is the sorted string, value would be the actual list of strs
        count_letter = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            count_letter[sorted_word].append(word)
        
        return list(count_letter.values())