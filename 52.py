class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiagonal=set()  
        negDiagonal=set()
        result = 0
        def backtrack(r):
            nonlocal result
            if r==n:
                result += 1
                return
            
            for c in range(n):
                if c not in cols and (r+c) not in posDiagonal and (r-c) not in negDiagonal:
                    cols.add(c)
                    posDiagonal.add(r+c)
                    negDiagonal.add(r-c)
                   
                    
                    backtrack(r+1)
                    cols.remove(c)
                    posDiagonal.remove(r+c)
                    negDiagonal.remove(r-c)
                    
                    
        backtrack(0)
        return result            