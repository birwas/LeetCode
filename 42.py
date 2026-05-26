class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = 0, 0
        water=0
        left=0
        right=len(height)-1
        while left<right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                water += max(0, leftMax - height[left])
                left+=1
            else:
                rightMax = max(rightMax, height[right])
                water+= max(0, rightMax - height[right])
                right-=1
        
        return water