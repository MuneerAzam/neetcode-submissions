class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always run binary search on the smaller array to guarantee O(log(min(m,n)))
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
            
        total_len = len(A) + len(B)
        half_len = total_len // 2
        
        left = 0
        right = len(A)
        
        # The search space is guaranteed to find a valid cut, so True is safe
        while True:
            i = (left + right) // 2   # Pointer for the cut in A
            j = half_len - i          # Forced pointer for the cut in B
            
            # Get the edges. If a cut is at index 0, there is nothing on the left (so -infinity).
            # If a cut is at the end of the array, there is nothing on the right (so +infinity).
            Aleft = A[i - 1] if i > 0 else float("-infinity")
            Aright = A[i] if i < len(A) else float("infinity")
            
            Bleft = B[j - 1] if j > 0 else float("-infinity")
            Bright = B[j] if j < len(B) else float("infinity")
            
            # Cross-check for the perfect partition
            if Aleft <= Bright and Bleft <= Aright:
                # If odd, the median is the smallest number sitting just to the right of the cut
                if total_len % 2 != 0:
                    return float(min(Aright, Bright))
                # If even, average the largest number on the left and smallest on the right
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                    
            # A's left edge is too big. We must move the partition left.
            elif Aleft > Bright:
                right = i - 1
            # A's left edge is too small. We must move the partition right.
            else:
                left = i + 1