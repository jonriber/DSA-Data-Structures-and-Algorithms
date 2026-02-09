
"""
    Given an unsorted array of integers nums
    Return the length of the longest sequence of consecutive integers

    Consecutive means x, x+1, x+2, ... etc
    with no gaps in between
"""
def longest_consecutive_sequence(nums):
    if not nums: 
        return 0
    
    longest_streak = 1

    num_set = set(nums)

    print(num_set)

    for num in num_set:
        if num-1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
    return longest_streak


