class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        nums.sort()
        def bt(start,total):
            if total==target:
                res.append(path[:])
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if total+nums[i]>target:
                    break
                path.append(nums[i])
                bt(i+1,total+nums[i])
                path.pop()
        bt(0,0)
        return res