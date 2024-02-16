## 326. Power of Three
'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        import math
        max_exponent: int = int(math.log((2 ** 31) - 1) / math.log(3))
        return (3 ** max_exponent) % n == 0
    
if __name__ == '__main__':
    output = Solution()
    print(output.isPowerOfThree(9))
    print(output.isPowerOfThree(11))

    # cannot use bit manipulation approach for this question to solve without loop/recursion
    # Need maths and the to take advantage of the limitation of n = 2^31 -1
    # This number is the largest number that can be stored in a signed 32-bit integer.
    # So, you find the largest exponent of 3 that can be stored in a 32-bit integer, lets call it m.
    # Then you return boolean of m % n == 0, to see if n is an exponent of 3.
    # This would be O(1) space and time.


