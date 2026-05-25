class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = longest = 0

        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                longest = max(longest, right * 2)
            elif right > left:
                left = right = 0

        left = right = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            if left == right:
                longest = max(longest, left * 2)
            elif left > right:
                left = right = 0

        return longest