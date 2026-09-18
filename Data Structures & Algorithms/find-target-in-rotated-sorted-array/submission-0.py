class Solution:
    def search(self, nums: List[int], target: int) -> int:
        max=nums[0]
        n=len(nums)
        offset=0
        for i in range(n):
            if nums[i]<max:
                offset=i
                break
        arr=nums[offset:n]+nums[0:offset]
        i=0
        n-=1
        while i<=n:
            mid=(i+n)//2
            if target>arr[mid]:
                i=mid+1
            elif target<arr[mid]:
                n=mid-1
            else:
                return (mid+offset)%len(nums)
        return -1