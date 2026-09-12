from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(prod(nums[:i]+nums[i+1:]))
        return res