class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left=0
        right=0
        counterLeftLeft=0
        counterLeftRight=0
        counterRightLeft=0
        counterRightRight=0
        longest = 0
        for i in range(len(s)):
            if s[i] == '(':
                counterLeftLeft += 1
            else:
                counterLeftRight += 1
            if counterLeftLeft == counterLeftRight:
                left +=1
                longest = max(longest, left*2)
            elif counterLeftRight > counterLeftLeft:
                counterLeftLeft = 0
                counterLeftRight = 0
                left = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                counterRightRight += 1
            else:
                counterRightLeft += 1
            if counterRightLeft == counterRightRight:
                right +=1
                longest = max(longest, right*2)
            elif counterRightLeft > counterRightRight:
                counterRightLeft = 0
                counterRightRight = 0
                right = 0
        return longest