## 171. Excel Sheet Column Number
'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

'''
# Difficulty: Easy
## Think of it like converting a base-26 number to base 10.

def titleToNumber(columnTitle: str) -> int:

    title_reversed = columnTitle[::-1]
    col_num: int = 0
    for i, letter in enumerate(title_reversed):
        col_num += (26**i * ((ord(letter))-ord("A")+1))

    return col_num


if __name__ == '__main__':
    print(titleToNumber("A"))
    print(titleToNumber("FXSHRXW"))
    print(titleToNumber("ZY"))
    print(titleToNumber("AHP"))
