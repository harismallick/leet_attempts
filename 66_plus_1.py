## 66. Plus One

'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''

# Difficulty: Easy

# Solution beats 84%

def plusOne(digits: list) -> list:
    carryover: int = 1
    i: int = 1
    position: int = len(digits) - i

    while carryover != 0:
        temp_num = digits[position]
        new_num = temp_num + 1
        if new_num == 10:
            digits[position] = 0
            carryover = 1
        elif new_num < 10:
            digits[position] = new_num
            carryover = 0

        if position == 0 and carryover == 1:
            digits.insert(0, 1)
            carryover = 0
        
        position -= 1

    return digits

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([4,9,9,9]))
print(plusOne([9]))
