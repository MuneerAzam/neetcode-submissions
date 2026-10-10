from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for s in strs:
            c=Counter(s)
            key=tuple(sorted(c.items()))
            group[key].append(s)
        return list(group.values())