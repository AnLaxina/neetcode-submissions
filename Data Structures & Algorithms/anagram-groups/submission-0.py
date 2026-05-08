from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            # Add each string as a particular set of words for anagram
            sorted_string = "".join(sorted(string))

            # For each sorted_string, make the key the sorted characters
            # And add the og string to the list
            anagrams[sorted_string].append(string)
        return anagrams.values()
