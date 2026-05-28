class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def combinations(start, current):
            result.append(current[:])
            for num in range(start, len(nums)):
                current.append(nums[num])
                combinations(num+1, current)
                current.pop()
        
        combinations(0, [])
        return result