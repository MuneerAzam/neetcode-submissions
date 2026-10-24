class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(x):
            return x == x[::-1]
        path = []
        res = []
        n = len(s)
        def bt(start):
            if start == n:
                res.append(path[:])
                return
            for i in range(start, n):
                sub = s[start:i+1]
                if isPalindrome(sub):
                    path.append(sub)
                    bt(i+1)
                    path.pop()
        bt(0)
        return res