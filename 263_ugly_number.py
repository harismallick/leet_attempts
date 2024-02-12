## 263. Ugly Number
'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        num = n

        while num != 1:
            if num % 2 == 0:
                num = num / 2
            elif num % 3 == 0:
                num = num / 3
            elif num % 5 == 0:
                num = num / 5
            else:
                return False

        return True
    
if __name__ == '__main__':
    output = Solution()
    print(output.isUgly(-2147483648))