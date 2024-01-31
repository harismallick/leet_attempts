## 168. Excel Sheet Column Title
'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

def convertToTitle(columnNumber: int) -> str:
    numbers = [x for x in range(1, 27)]
    letters_ascii = [x for x in range(65, 91)]
    number_to_letter: dict = {}
    for i in range(0, len(numbers)):
        number_to_letter[numbers[i]] = chr(letters_ascii[i])

    excel_col: str = ""
    while columnNumber > 0:
        quotient = columnNumber // 26
        remainder = columnNumber % 26
        if remainder != 0:
            excel_col = number_to_letter[remainder] + excel_col
            columnNumber = quotient
        else:
            excel_col = "Z" + excel_col
            columnNumber = quotient - 1

    # excel_col = number_to_letter[columnNumber] + excel_col
    return excel_col

if __name__ == '__main__':

    print(convertToTitle(900))
    print(convertToTitle(703))
