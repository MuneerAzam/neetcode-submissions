class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=sorted(nums)
        result=set()
        for k in range(len(nums)):
            i=k+1
            j=len(n)-1
            while i<j:
                if n[i]+n[j]+n[k]>0:
                    j-=1
                elif n[i]+n[j]+n[k]<0:
                    i+=1
                else:
                    result.add(tuple(sorted([n[i],n[j],n[k]])))
                    i+=1
                    j-=1
        return list(result)