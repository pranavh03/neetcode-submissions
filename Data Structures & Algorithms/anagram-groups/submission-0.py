class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sortin=''.join(sorted(s))
            res[sortin].append(s)
        return list(res.values())
        
        