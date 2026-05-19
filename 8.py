class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX =  2**31 - 1   #  2147483647
        INT_MIN = -(2**31)     # -2147483648

        i = 0
        n = len(s)

        # Step 1: skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: check sign
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: read digits
        rev = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Step 4: check overflow before committing
            if rev > INT_MAX // 10:
                return INT_MAX if sign == 1 else INT_MIN
            if rev == INT_MAX // 10 and digit > 7:
                return INT_MAX if sign == 1 else INT_MIN

            rev = rev * 10 + digit
            i += 1

        return sign * rev  