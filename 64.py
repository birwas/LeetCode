class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        pathSum=[[0] * n for _ in range(m)]
        pathSum[0][0]=grid[0][0]
        for i in range(1,m):
            pathSum[i][0]=pathSum[i-1][0]+grid[i][0]
        for j in range(1,n):
            pathSum[0][j]=pathSum[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                pathSum[i][j]=min(pathSum[i-1][j],pathSum[i][j-1])+grid[i][j]
        return pathSum[-1][-1]