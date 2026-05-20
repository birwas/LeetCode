def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
    nums = sorted(nums)
    result = []

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]:  
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j-1]:  
                continue

            L = j + 1
            R = len(nums) - 1

            while L < R:
                s = nums[i] + nums[j] + nums[L] + nums[R]
                if s == target:
                    result.append([nums[i], nums[j], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]: L += 1
                    while L < R and nums[R] == nums[R-1]: R -= 1
                    L += 1
                    R -= 1
                elif s < target:
                    L += 1
                else:
                    R -= 1

    return result