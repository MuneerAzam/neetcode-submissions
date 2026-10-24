from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def sub(n):
            if n == 0:
                return 0
            if n < 0:
                return float('inf')
            count = float('inf')
            for c in coins:
                count = min(count, 1 + sub(n - c))
            return count
        ans = sub(amount)
        return -1 if ans == float('inf') else ans