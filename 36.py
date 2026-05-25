class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[(row // 3) * 3 + col // 3]:
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[(row // 3) * 3 + col // 3].add(board[row][col])
        return True