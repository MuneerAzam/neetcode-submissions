class Solution:

    def encode(self, strs: List[str]) -> str:
        key='*#$%*'
        if not strs:
            return 'X'
        else:
            return key.join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="X":
            return []
        key='*#$%*'
        return s.split(key)
