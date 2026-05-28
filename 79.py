class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if board[i][j] != word[k]:
                return False
            
            board[i][j] = '#'
            for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                if dfs(i+x, j+y, k+1):
                    return True
            board[i][j] = word[k]
            return False
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
            