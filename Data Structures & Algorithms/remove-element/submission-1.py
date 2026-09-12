class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==1 and nums[0]==val:
            return 0
        n=len(nums)
        decrement=0
        try:
            for i in range(n):
                if nums[i]==val:
                    nums[i-decrement]=nums[i+1]
                    decrement+=1
                else:
                    nums[i-decrement]=nums[i]
        except:
            decrement+=1
            return n-decrement
        return n-decrement

        