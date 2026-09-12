class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        count=1
        max=1
        prev=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==prev+1:
                count+=1
                if count>max:
                    max=count
            else:
                count=1
            prev=nums[i]
        return max