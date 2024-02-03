## 202. Happy Number
'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
'''

def isHappy(n: int) -> bool:
    # if n <= 0:
    #     return False
    
    # cached_nums: list = []
    # while n not in cached_nums:
    #     cached_nums.append(n)
    #     string_of_num: str = str(n)
    #     n = 0
    #     for num in string_of_num:
    #         n += int(num) ** 2

    #     if n == 1:
    #         return True
    # return False
# My solution is only faster than 30% of submissions
# Lets try a solution where we don't convert the int into a string:
    if n <= 0:
        return False
    
    cached_nums: list = []
    while n not in cached_nums:
        cached_nums.append(n)
        new_num: int = 0
        while n > 0:
            remainder: int = n % 10
            new_num += remainder ** 2
            n = int(n/10)
        n = new_num

        if n == 1:
            return True
    return False
# This solution faster than 87% of submissions!
# Lesson: Converting int to string slows down the algorithm. Try to maintain constant data type if possible in the algorithm.
# Floyd's Cycle Finding algo can be applied for a solution with O(1) space complexity.

if __name__ == '__main__':
    print(isHappy(19))