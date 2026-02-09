
"""
    Given an unsorted array of integers nums
    Return the length of the longest sequence of consecutive integers

    Consecutive means x, x+1, x+2, ... etc
    with no gaps in between
"""
def longest_consecutive_sequence(nums):
    if not nums: 
        return 0
    
    longest_streak = 0

    num_set = set(nums)

    # print(num_set)

    for num in num_set:
        if num-1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
    return longest_streak


## dev notes while studying this problem:
# 1. If I sort the array, I am adding O(n log n) complexity, which is not ideal
# 2. sort alone is O(n log n), looping through the sorted array is O(n), so total complexity would be O(n log n) + O(n) = O(n log n)
# 3. Using a set to store the numbers from the array, let me work with O(n) complexity for building the set, and then O(n) for looping through the set, so total complexity would be O(n) + O(n) = O(n)
# 4. Set removes duplicates, but does not sort the numbers, so I can still find the longest consecutive sequence without worrying about duplicates
# 5. the best candidate to start looking for a sequence in the set is a number that does not have a predecessor (num-1), because if it has a predecessor, then it is not the start of a sequence
# 6. Once I find a number that does not have a predecessor, I can keep checking for the next number in the sequence (current_num + 1) until I find a number that is not in the set, which means I have reached the end of the sequence
# 7. I can keep track of the longest streak found so far and update it whenever I find a longer streak
