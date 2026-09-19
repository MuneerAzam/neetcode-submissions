class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=len(s1)
        n=len(s2)
        if m>n:
            return False
        s1c=[0]*26
        win=[0]*26
        for i in range(m):
            s1c[ord(s1[i])-97]+=1
            win[ord(s2[i])-97]+=1
        if s1c==win:
            return True
        for i in range(m,n):
            win[ord(s2[i-m])-97]-=1
            win[ord(s2[i])-97]+=1
            if s1c==win:
                return True
        return False