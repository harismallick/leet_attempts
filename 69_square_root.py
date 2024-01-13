## 69. Sqrt(x)
'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''

# Difficulty: Easy
# Poor solution - Only beats 5% of users

# def mySqrt(x: int) -> int:
#     i = 0

#     while i*i < x:
#         if (i+1)*(i+1) > x:
#             return i
#         i += 1

#     return i

## Reduce time complexity from O(N) to O(nlogn) with binary search
# This solution beats 83% of submissions

def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    start = 0
    end = x

    while int(start) < int(end):
        middle = (start + (end)) / 2

        if middle*middle > x:
            end = middle
        elif middle*middle < x:
            start = middle
        elif middle*middle == x:
            return int(middle)

    return int(start)

print(mySqrt(4))
print(mySqrt(9))
print(mySqrt(900))
print(mySqrt(1050))
print(mySqrt(10505))


