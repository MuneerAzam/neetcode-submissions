class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)
        res=j
        while i<=j:
            mid=(i+j)//2
            th=0
            for p in piles:
                th+=math.ceil(p/mid)
            if th<=h:
                res=mid
                j=mid-1
            else:
                i=mid+1
        return res