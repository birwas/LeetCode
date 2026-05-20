class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        symbols = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        result = ['']
        for digit in digits:
            result = [prefix + char for prefix in result for char in symbols[digit]]
        return result
    