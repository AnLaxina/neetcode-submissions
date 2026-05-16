class Solution:

    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False
        else:
            s_map = {}
            t_map = {}
            for i in range(len(s)):
                s_map[s[i]] = s_map.get(s[i], 0) + 1
                t_map[t[i]] = t_map.get(t[i], 0) + 1
            return t_map == s_map

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
            
            for val in my_map.values():
                arr_return.append(val)
            


            return arr_return
                