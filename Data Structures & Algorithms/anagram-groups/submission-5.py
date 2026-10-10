from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        track=[[0]*130 for i in range(len(strs))]
        for i,a in enumerate(strs):
            for j in a:
                track[i][ord(j)]+=1
            dict[tuple(track[i])].append(a)
        return list(dict.values())