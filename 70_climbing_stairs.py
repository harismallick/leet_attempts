## 70. Climbing Stairs
'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

# Difficulty: Easy
# This is a binary tree problem. Build tree and find all leaf nodes

# Naive solution:
# Time limit exceeded
# def result(n: int) -> int:
#     num_set: set = {0,1,2}
#     num_list: list = [n]

#     while len(num_set) != 1:
#         temp_list = []
#         while len(num_list) > 0:
#             current_num: int = num_list.pop()
#             if current_num == 0:
#                 temp_list.append(current_num)
#                 continue
#             num1 = current_num - 1
#             num2 = current_num - 2
#             if num1 >= 0:
#                 temp_list.append(num1)
#             if num2 >= 0:
#                 temp_list.append(num2)

#         num_list = temp_list
#         temp_list = []
#         num_set = set(x for x in num_list)
#     return len(num_list)

# Simple recursion also too slow. Time limit exceeded on n >= 44

# def result(n: int) -> int:

#     if n == 0 or n == 1:
#         return 1
    
#     return result(n-1) + result(n-2)

# Recursion + memoisation needed
def result(n: int) -> int:
    memo = {}
    return helper(n, memo)

def helper(n: int, memo: dict[int, int]) -> int:
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = helper(n-1, memo) + helper(n-2, memo)
    return memo[n]

print(result(3))
print(result(5))
print(result(35))
