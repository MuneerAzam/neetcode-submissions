from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        res=[]
        for i in range(l):
            res.append(prod(nums[:i]+nums[i+1:]))
        return res