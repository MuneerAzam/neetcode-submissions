def check(arr):
        max=0
        for a in arr:
            if a>max:
                max=a
        return max
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[]
        max=check(arr)
        for i in range(n-1):
            if arr[i]==max:
                max=check(arr[i+1:])
            res.append(max)
        res.append(-1)
        return res