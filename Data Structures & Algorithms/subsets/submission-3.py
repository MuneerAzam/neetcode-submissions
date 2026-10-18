class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path=[]
        res=[]
        def solve(start):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                solve(i+1)
                path.pop()
        solve(0)
        return res