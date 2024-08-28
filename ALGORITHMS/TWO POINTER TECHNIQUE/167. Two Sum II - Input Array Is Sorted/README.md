# 167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

## Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


## Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].


## Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

## Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

## Solution key points

  numbers = [2, 7, 11, 15]
  target = 9

### Initial Pointers:

- left = 0, right = 3
- numbers[left] = 2, numbers[right] = 15
- current_sum = 2 + 15 = 17

### Check current_sum:

- current_sum (17) is greater than target (9), so move the right 
pointer to the left.
- right = 2

### Second Iteration:

- left = 0, right = 2
- numbers[left] = 2, numbers[right] = 11
- current_sum = 2 + 11 = 13

### Check current_sum:

- current_sum (13) is still greater than target (9), so move the right pointer 
to the left again.
- right = 1

### Third Iteration:

- left = 0, right = 1
- numbers[left] = 2, numbers[right] = 7
- current_sum = 2 + 7 = 9

### Check current_sum:

- current_sum (9) equals target (9). We've found the solution!
- Return [left + 1, right + 1] = [1, 2].