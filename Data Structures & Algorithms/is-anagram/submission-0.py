class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        for a in s:
            if a in dic1:
                dic1[a]+=1
            else:
                dic1[a]=1
        for b in t:
            if b in dic2:
                dic2[b]+=1
            else:
                dic2[b]=1
        if dic1==dic2:
            return True
        else:
            return False