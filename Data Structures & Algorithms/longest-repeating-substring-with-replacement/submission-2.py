from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j=0
        dic=defaultdict(int)
        m=0
        for i,a in enumerate(s):
            dic[a]+=1
            freq=max(dic.values())
            while i-j-freq+1>k:
                dic[s[j]]-=1
                j+=1
                freq=max(dic.values())
            m=max(m,i-j+1)
        return m
            