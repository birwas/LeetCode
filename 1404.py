class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        for i in range(len(s) -1 , 0 , -1):
            bit = int(s[i]) + carry
            if bit == 1: #odd
                steps += 2
                carry = 1
            else: #even
                steps += 1 
                carry = 1 if bit== 2 else 0
        
        return steps + carry