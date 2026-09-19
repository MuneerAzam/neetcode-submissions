from collections import Counter
class Solution:
    def c(a,b):
        for s in a:
            if a[s]<b[s]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        check=Counter(t)
        m=len(s)    
        j=0
        res=[0,0]
        win=dict.fromkeys(check,0)
        flag=0
        min_l=float('inf')
        for i,a in enumerate(s):
            if a in win:
                win[a]+=1
            while Solution.c(win,check):
                flag=1
                cw=i-j+1
                if cw<min_l:
                    res[0]=j
                    res[1]=i
                    min_l=cw
                if s[j] in win:
                    win[s[j]]-=1
                j+=1
        if flag:
            return s[res[0]:res[1]+1]
        else:
            return ""