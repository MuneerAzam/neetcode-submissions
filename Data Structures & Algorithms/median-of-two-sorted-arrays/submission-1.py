class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        n=len(nums1)+len(nums2)
        for i in range(n):
            if not nums1:
                arr.append(nums2.pop(0))
            elif not nums2:
                arr.append(nums1.pop(0))
            elif nums1[0]<nums2[0]:
                arr.append(nums1.pop(0))
            else:
                arr.append(nums2.pop(0))
        if n%2==0:
            return (arr[(n//2)-1]+arr[n//2])/2
        else:
            return float(arr[(n//2)])