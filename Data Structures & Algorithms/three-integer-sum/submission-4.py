class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=sorted(nums)
        result=set()
        for k in range(len(nums)):
            if k > 0 and n[k] == n[k - 1]:
                continue
            i=k+1
            j=len(n)-1
            while i<j:
                total = n[i] + n[j] + n[k]
                if total>0:
                    j-=1
                elif total<0:
                    i+=1
                else:
                    result.add(tuple([n[i],n[j],n[k]]))
                    i+=1
                    j-=1
        return list(result)