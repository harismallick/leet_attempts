## 338. Counting Bits
'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''

class Solution:
    def countBits(self, n: int) -> list[int]:
        # ones_arr: list = []
        # for i in range(0, n+1):
        #     binary: str = bin(i)
        #     one_count: int = binary.count("1")
        #     ones_arr.append(one_count)
        # return ones_arr
    
    # actual solution:
        ones_arr: list = [0]* (n+1)
        for i in range(1, n+1):
            count: int = ones_arr[i >> 1] + (i & 1)
            ones_arr[i] = count
            # print(count)

        return ones_arr
'''
Dynamic Programming with Bit Manipulation
In this approach, we exploit the fact that shifting a number to the right by one bit (i.e., dividing by 2) removes the last bit. So, the number of 1's in the binary representation of i is the same as (number of 1s in i/2) plus the last bit of i (either 0 or 1).
'''
if __name__ == '__main__':
    output = Solution()
    # print(bin(100000))
    print(output.countBits(5))

