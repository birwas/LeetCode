class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums= sorted(nums)
        closestSum = float('inf')
        for i in range(len(nums) - 2):
            L, R = i + 1, len(nums) - 1
            while L < R:
                currSum = nums[i] + nums[L] + nums[R]
                if abs(currSum - target) < abs(closestSum - target):
                    closestSum = currSum
                if currSum < target:
                    L += 1
                elif currSum > target:
                    R -= 1
                else:
                    return target
        return int(closestSum)