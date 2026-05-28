class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest=0
        stack=[]
        for i,h in enumerate(heights):
            while stack and stack[-1][1] > h:
                index, height =stack.pop()
                left = stack[-1][0] if stack else -1
                width = i-left-1
                largest=max(largest, height*width)
            stack.append((i,h))
        
        
        while stack:
            index, height =stack.pop()
            left = stack[-1][0] if stack else -1
            width = len(heights)-left-1
            largest=max(largest, height*width)
        return largest