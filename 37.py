class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """ 
        def candidates(board, r, c):
            seen = set()
            for i in range(9):
                seen.add(board[r][i])    
                seen.add(board[i][c])    
                seen.add(board[3*(r//3) + i//3][3*(c//3) + i%3])  
            return set('123456789') - seen
        
        def solve(board, emptyCells):
            if not emptyCells:
                return True
            
            r, c = min(emptyCells, key=lambda cell: len(candidates(board, *cell)))
            emptyCells.remove((r, c))
            
            for digit in candidates(board, r, c):
                board[r][c] = digit
                if solve(board, emptyCells):
                    return True
                board[r][c] = '.'
            
            emptyCells.add((r, c))
            return False
        
        emptyCells = {(r, c) for r in range(9) for c in range(9) if board[r][c] == '.'}
        solve(board, emptyCells)