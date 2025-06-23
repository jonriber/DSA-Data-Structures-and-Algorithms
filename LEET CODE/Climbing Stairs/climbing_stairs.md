# Climbing stairs - LeetCode

link: <https://leetcode.com/problems/climbing-stairs/description/>

## Description

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Examples

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

## Logic and step-by-step solution

Asking myself: what are the possible number of ways to reach step n (final destination)?

`f(n)` = number of distinct ways to reach step n

`f(0)` = 1 -> do nothing

`f(1)` = 1 -> single step

`f(2)` = 2 -> two steps

Start with this (base Case):

```python
f(0) = 1
f(1) = 1
f(2) = 2

```

Identify the recurrence relation

To reach final destination or `step n` one could:

- come from step n-1 by taking 1 step, or
- come from step n-2 by taking 2 steps

```python

f(n) = f(n - 1) + f(n - 2)

```