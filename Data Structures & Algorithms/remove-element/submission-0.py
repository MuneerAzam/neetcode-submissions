class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        decrement=0
        k=0
        for i in range(n):
            nums[i-decrement]=nums[i]
            k+=1
            if nums[i]==val:
                decrement+=1
                k-=1        
        return k
