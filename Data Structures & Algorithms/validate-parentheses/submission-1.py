class Solution:
    def isValid(self, s: str) -> bool:
        start=0
        res=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                res.append(i)
                start+=1
            else:
                if i==')':
                    if start==0:
                        return False
                    if res[-1]!='(':
                        return False
                    else:
                        res.pop()
                        start-=1
                elif i=='}':
                    if start==0:
                        return False
                    if res[-1]!='{':
                        return False
                    else:
                        res.pop()
                        start-=1
                elif i==']':
                    if start==0:
                        return False
                    if res[-1]!='[':
                        return False
                    else:
                        res.pop()
                        start-=1
        if not res:
            return True
        else:
            return False