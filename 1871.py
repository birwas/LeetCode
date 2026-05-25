class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        n = len(s)
        diff = [0] * (n + 1)
        diff[minJump] += 1
        diff[maxJump + 1] -= 1

        reach = 0
        for i in range(1, n):
            reach += diff[i]
            if reach > 0 and s[i] == '0':
                if i == n - 1:
                    return True
                if i + minJump < n:
                    diff[i + minJump] += 1
                if i + maxJump + 1 < n:
                    diff[i + maxJump + 1] -= 1

        return False
            