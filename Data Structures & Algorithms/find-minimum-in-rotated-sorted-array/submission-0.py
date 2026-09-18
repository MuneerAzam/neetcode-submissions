class Solution:
    def findMin(self, nums: List[int]) -> int:
        max=nums[0]
        offset=0
        for i in range(len(nums)):
            if nums[i]<max:
                offset=i
                break
        return nums[offset]