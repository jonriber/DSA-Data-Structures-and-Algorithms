# Jump Game - Leetcode

Link: <https://leetcode.com/problems/jump-game/description/>

## Description

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

## Examples

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible 
to reach the last index.

## Solution

- `max_reach` keeps track of the farthest reachable index
- At each index i, check if its within max_reach
- if not, index can not be reachable, and so, return False
- If it is possible to make to the end of the loop, than return True