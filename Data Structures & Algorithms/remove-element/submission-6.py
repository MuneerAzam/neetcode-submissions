class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        decrement=0
        try:
            for i in range(n):
                if nums[i-decrement]==val:
                    nums.remove(nums[i-decrement])
                    decrement+=1
        except:
            return len(nums)
        return len(nums)
