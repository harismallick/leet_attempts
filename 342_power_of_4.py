## 342. Power of Four
'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            lookup = [32, 0, 1, 26, 2, 23, 27, 0, 
                3, 16, 24, 30, 28, 11, 0, 13,
                4, 7, 17, 0, 25, 22, 31, 15,
                29, 10, 12, 6, 0, 21, 14, 9,
                5, 20, 8, 19, 18] 
            if n & n-1 == 0:
                if lookup[(n & -n)%37] % 2 == 0:
                    return True
        return False

# Beats 89%
# Here's the solution I used to count trailing 0s in a byte:
# https://www.geeksforgeeks.org/count-trailing-zero-bits-using-lookup-table/ 
    
if __name__ == '__main__':
    output = Solution()
    print(output.isPowerOfFour(8))
    # num1 = 16
    # num2 = 3
    # lookup = [32, 0, 1, 26, 2, 23, 27, 0, 
    #           3, 16, 24, 30, 28, 11, 0, 13,
    #           4, 7, 17, 0, 25, 22, 31, 15,
    #           29, 10, 12, 6, 0, 21, 14, 9,
    #           5, 20, 8, 19, 18] 
    # print(num1 & num2)
    # print(lookup[(num1 & -num1)%37])
    # print(len(bin(2**31 - 1)))

