from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = Counter(word)

            key = tuple(sorted(count.items()))

            groups[key].append(word)

        return list(groups.values())