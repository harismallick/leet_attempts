## 258. Add digits
'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 != 0:
            return num % 9
        return 9

if __name__ == '__main__':
    output = Solution()
    print(output.addDigits(81))