## 118. Pascal's Triangle
'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown.
'''

# Difficulty: Easy

def generate(numRows: int) -> list[list[int]]:
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    output: list = [[1], [1,1]]
    current_level = 3
    j = 1
    while current_level <= numRows:
        temp_list = [1] * current_level
        previous_list = output[current_level-2]
        while j < len(previous_list):
            temp_list[j] = previous_list[j] + previous_list[j-1]
            j += 1
        output.append(temp_list)
        j = 1
        current_level += 1

    return output

# Recursive solution:

    # if numRows == 0:
    #     return []
    # if numRows == 1:
    #     return [[1]]
    
    # prevRows = generate(numRows - 1)
    # newRow = [1] * numRows
    
    # for i in range(1, numRows - 1):
    #     newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
    
    # prevRows.append(newRow)
    # return prevRows

if __name__ == '__main__':
    print(generate(5))