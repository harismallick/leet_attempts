'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

# Difficulty: Easy

# My solution:
# Create a stack of opening brackets, removed from stack if closing bracket encoutered

def isValid(s: str) -> bool:

    hashmap: dict = {
        ")":"(",
        "]": "[",
        "}": "{"
    }
    if len(s) % 2 != 0:
        return False
    
    queue = []
    for bracket in s:
        if bracket in hashmap.keys():
            if len(queue) == 0 or queue[-1] != hashmap[bracket]:
                return False
            queue.pop()
            continue

        queue.append(bracket)

    if len(queue) == 0:
        return True
    
    return False

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("){"))
print(isValid("{[]}"))
print(isValid("{[()]}"))

