import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        nums=(1,2,3,4,5,6,7,8,9)
        for i in range(n):
            if len([x for x in board[i] if x!='.'])!=len(set([x for x in board[i] if x!='.'])):
                return False

        for i in range(n):
            column=[row[i] for row in board]
            if len([x for x in column if x!='.'])!=len(set([x for x in column if x!='.'])):
                return False       
        for i in range(0,9,3):
            for j in range(0,9,3):
                mat=[row[j:j+3] for row in board[i:i+3]]
                a=np.array(mat)
                a=a.flatten()
                a=[x for x in a if x!='.']
                if len(a)!=len(set(a)):
                    return False
        return True