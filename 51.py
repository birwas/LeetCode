from ast import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiagonal=set()  
        negDiagonal=set()
        
        board = [["."]*n for _ in range(n)]
        result = []
        def backtrack(r):
            if r==n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c not in cols and (r+c) not in posDiagonal and (r-c) not in negDiagonal:
                    cols.add(c)
                    posDiagonal.add(r+c)
                    negDiagonal.add(r-c)
                    board[r][c] = "Q"
                    
                    backtrack(r+1)
                    cols.remove(c)
                    posDiagonal.remove(r+c)
                    negDiagonal.remove(r-c)
                    board[r][c] = "."
                    
        backtrack(0)
        return result            