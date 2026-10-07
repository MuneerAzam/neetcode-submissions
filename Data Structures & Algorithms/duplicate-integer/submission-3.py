class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rep=set()
        for i in nums:
            if i in rep:
                return True
            rep.add(i)
        return False