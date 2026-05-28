class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n=len(matrix[0])
        heights=[0]* (n+1)
        maxArea=0
        
        for row in matrix:
            for c in range(n):
                heights[c]=heights[c]+1 if row[c]=="1" else 0
                
            stack=[-1]
            for i in range(n+1):
                while stack[-1]!= -1 and heights[i]<heights[stack[-1]]:
                    h=heights[stack.pop()]
                    w=i-stack[-1]-1
                    maxArea=max(maxArea,h*w)
                stack.append(i)
        return maxArea