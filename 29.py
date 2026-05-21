class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        count=0
        while a >= b:
            temp,multiplier = b,1
            while a >= (temp << 1):
                temp <<= 1
                multiplier <<= 1
            a -= temp
            count += multiplier
        if negative:
            count = -count
        
        return min(max(-2**31, count), 2**31 - 1)