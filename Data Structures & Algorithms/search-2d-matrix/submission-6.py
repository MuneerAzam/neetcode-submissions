class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        r=len(matrix)
        c=len(matrix[0])
        j=(r*c)-1
        while i<=j:
            mi=(i+j)//2
            mid=matrix[mi//c][mi%c]
            if mid>target:
                j=mi-1
            elif mid<target:
                i=mi+1
            else:
                return True
        return False