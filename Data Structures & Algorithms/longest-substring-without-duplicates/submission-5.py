class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mc=0
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        j=0
        check={}
        for i,a in enumerate(s):
            if a in check and check[a]>=j:
                j=check[a]+1
            check[a]=i
            c=i-j+1
            mc=max(mc,c)
        return mc