## 119. Pascal's Triangle II
'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown.
'''

def getRow(rowIndex: int) -> list[int]:
    if rowIndex+1 == 1:
        return [1]
    if rowIndex+1 == 2:
        return [1,1]
    
    previous_list: list = [1,1]
    i: int = 3
    while i <= rowIndex+1:
        current_list: list = [1]*i
        for j in range(1, len(previous_list)):
            current_list[j] = previous_list[j] + previous_list[j-1]
        if i == rowIndex+1:
            return current_list
        i += 1
        previous_list = current_list


if __name__ == '__main__':
    print(getRow(3))