from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)
        arr = []

        for i in strs:
            n = tuple(sorted(i))
            hashmap[n].append(i)

        for i in hashmap.values():
            arr.append(i)

        return arr