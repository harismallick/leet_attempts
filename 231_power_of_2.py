## 231. Power of Two
'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
'''
# Difficulty: Easy
# Challenge: Can you do it without using loops or recursion?

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n & n-1 == 0:
            return True
        return False

if __name__ == '__main__':
    n: int = 15
    solution = Solution()
    print(solution.isPowerOfTwo(n))