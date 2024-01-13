## 67. Add Binary

'''
Given two binary strings a and b, return their sum as a binary string.
'''

# Difficulty: Easy
# Beats 65% of results

# def addBinary(a: str, b: str) -> str:

#     def intToBinary(num: int) -> str:
#         if num == 0:
#             return "0"
        
#         bin_list: list[str] = []
#         remainder: int = 0
#         quotient: int = num

#         while quotient != 0:
#             remainder = quotient % 2
#             quotient = quotient // 2
#             bin_list.insert(0, str(remainder))
#         return "".join(bin_list)
    
#     num1: int = int(a, 2)
#     num2: int = int(b, 2)
#     nums_sum: int = num1 + num2
#     sum_binary: str = intToBinary(nums_sum)

#     return sum_binary

# Slightly faster 2-pointer solution
# Beats 75% or results

def addBinary(a: str, b: str) -> str:

    sum_binary: str = ""

    i: int = len(a) - 1
    j: int = len(b) - 1
    carry = 0
    while i >= 0 or j >= 0:
        sum: int = carry
        if i >= 0:
            sum += int(a[i])
        if j >= 0:
            sum += int(b[j])
        
        if sum >= 2:
            carry = 1
        else:
            carry = 0

        sum_binary += str(sum % 2)
        i -= 1
        j -= 1

    if carry == 1:
        sum_binary += "1"

    return sum_binary[::-1]

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
print(addBinary("0", "0"))
