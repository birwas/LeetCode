class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums[0] == nums[-1]:
            while  nums[0] == nums[-1] and len(nums)>1:
                nums.pop()
            if  len(nums) == 1:
                return True
        rotated =   sum(nums[i]> nums[i+1] for i in range(len(nums)-1))
        return rotated <= 1