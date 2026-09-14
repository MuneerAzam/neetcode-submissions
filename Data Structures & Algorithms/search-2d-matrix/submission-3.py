class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        # Pointers for our imaginary 1D array
        left = 0
        right = (ROWS * COLS) - 1 
        
        while left <= right:
            mid = (left + right) // 2
            
            # Translate the 1D 'mid' index back into a 2D row and column
            row = mid // COLS
            col = mid % COLS
            
            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True
                
        return False