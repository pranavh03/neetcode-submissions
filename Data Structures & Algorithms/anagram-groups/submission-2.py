class Solution:
    from collections import Counter
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dictionary=defaultdict(list)
        for word in strs:
            key=''.join(sorted(word))
            Dictionary[key].append(word)
        return [i for i in Dictionary.values()]


        