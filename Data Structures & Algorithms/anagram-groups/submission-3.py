class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        else:
            my_map = {}
            arr_return = []
            for word in strs:
                list_word = sorted(list(word))
                key = "".join(list_word)
                if key not in my_map:
                    my_map[key] = []
                my_map[key].append(word)
            
        
            return list(my_map.values())
                