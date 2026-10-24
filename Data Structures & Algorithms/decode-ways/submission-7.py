
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        dp = [0] * n
        dp[0] = 1
        if n == 1:
            return dp[0]
        dp[1] = (1 if s[1] != '0' else 0) + (1 if 10 <= int(s[0:2]) <= 26 else 0)
        for i in range(2, n):
            a = 1 if s[i] != '0' else 0
            b = 1 if 10 <= int(s[i-1:i+1]) <= 26 else 0
            if a:
                dp[i] += dp[i-1]
            if b:
                dp[i] += dp[i-2]
        return dp[n-1]
