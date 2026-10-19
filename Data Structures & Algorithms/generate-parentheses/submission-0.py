class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        path=[]
        def bt(o,c):
            if len(path)==2*n:
                res.append("".join(path))
                return
            if o<n:
                path.append('(')
                bt(o+1,c)
                path.pop()
            if o>c:
                path.append(')')
                bt(o,c+1)
                path.pop()
        bt(0,0)
        return res
            