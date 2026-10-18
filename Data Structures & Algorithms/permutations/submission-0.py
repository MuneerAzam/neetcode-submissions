class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n=len(nums)
        def bt():
            if len(path)==n:
                res.append(path[:])
            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                bt()
                path.pop()
        bt()
        return res