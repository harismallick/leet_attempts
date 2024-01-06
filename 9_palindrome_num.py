'''
Given an integer x, return true if x is a 
palindrome, and false otherwise.
'''

# Difficulty : Easy
# Challenge: Do it without converting num to string

# My solution:
# def isPalindrome(x: int) -> bool:

#     quotient: int = x
#     base_10 = 1
#     split_num: list = []
#     base_track: list = []
#     while quotient > 0:
#         remainder: int = quotient % 10
#         split_num.append(remainder)
#         base_track.append(base_10)
#         quotient = int(quotient / 10)
#         base_10 = base_10 * 10

#     reversed_num: int = 0
#     for i, num in enumerate(reversed(base_track)):
#         reversed_num = reversed_num + (split_num[i] * num)
    
#     if reversed_num == x:
#         return True
    
#     return False

# More optimal solution:
def isPalindrome(x: int) -> bool:

    quotient: int = x
    reversed_num = 0
    while quotient > 0:
        remainder: int = quotient % 10
        reversed_num: int = (reversed_num * 10) + remainder
        quotient = int(quotient / 10)

    if reversed_num == x:
        return True
    
    return False

print(isPalindrome(121))
# print(int(189 / 10))