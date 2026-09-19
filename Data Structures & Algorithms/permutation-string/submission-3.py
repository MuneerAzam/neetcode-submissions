from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tar=Counter(s1)
        m=len(s1)
        n=len(s2)
        if m==n:
            return tar==Counter(s2)
        for i in range(m,n+1):
            if Counter(s2[i-m:i])==tar:
                return True
        return False