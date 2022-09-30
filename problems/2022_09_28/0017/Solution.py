class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def dsf(i, curr):
            if i >= len(digits):
                res.append(curr)
                return

            for c in mapping[digits[i]]:
                dsf(i+1, curr + c)

        dsf(0, '')

        return res
