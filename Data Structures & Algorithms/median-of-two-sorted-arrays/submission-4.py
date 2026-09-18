class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        n=len(nums1)+len(nums2)
        a=0
        b=0
        for i in range(n):
            if a==len(nums1):
                arr.append(nums2[b])
                b+=1
            elif b==len(nums2):
                arr.append(nums1[a])
                a+=1
            elif nums1[a]<nums2[b]:
                arr.append(nums1[a])
                a+=1
            else:
                arr.append(nums2[b])
                b+=1
        if n%2==0:
            return (arr[(n//2)-1]+arr[n//2])/2
        else:
            return float(arr[(n//2)])