'''
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.
'''

# Difficulty: Hard
## Need to learn trees datastructure for this challenge
## Revisit once finishing datastructure tutorial

def jobScheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:

    tuple_arr: list = []
    i = 0
    while i < len(startTime):
        tuple_arr.append((startTime[i], endTime[i], profit[i]))
        i += 1

    max_profit: int = 0
    for item in tuple_arr:
        temp_profit: int = 0
        end_time: int = 0
        for tup in tuple_arr:
            if end_time <= tup[0]:
                temp_profit += tup[2]
                end_time = tup[1]

        if temp_profit > max_profit:
            max_profit = temp_profit

        temp_profit = 0
        end_time = 0

    return max_profit

print(jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))