class Solution:

    def encode(self, strs: List[str]) -> str:
        key='*#$%*'
        e='^%#$^%$^%#^%#^%'
        if not strs:
            return e
        else:
            return key.join(strs)

    def decode(self, s: str) -> List[str]:
        key='*#$%*'
        e='^%#$^%$^%#^%#^%'
        if s==e:
            return []
        return s.split(key)
