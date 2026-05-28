class Solution:
    def sortcolors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colours = [0, 0, 0]
        for num in nums:
            colours[num] += 1
            
        index = 0
        for colour in range(3):
            for _ in range(colours[colour]):
                nums[index] = colour
                index += 1