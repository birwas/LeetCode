class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                m1 = ord(num1[i]) - ord('0')
                m2 = ord(num2[j]) - ord('0')
                product = m1 * m2 + result[i + j + 1]
                result[i + j + 1] = product % 10
                result[i + j] += product // 10
        
        output= ''.join(map(str, result)).lstrip('0') or '0'
        return output
        