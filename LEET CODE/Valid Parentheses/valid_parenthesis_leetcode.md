# Valid Parenthesis - Leetcode

Link: <https://leetcode.com/problems/valid-parentheses/description/>

## Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

## Examples

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

## Solving strategy

Using a stack to store opening brackets. For every closing bracket, check if it matches the last opening bracket in 
the stack.

### Stack

Stack is a linear data structure that follows the principle of:

`LIFO = Last in, first out`

Common stack operations

- Push(x) - add item x to the last position, top
- pop() - remove and return the last (top) item
- peek() - look at the top item
- isEmpty() - check if stack is empty

Analogy:

- stack is like a pile of plates
- we put new plates on top (push)
- you remove the top plate when needed (pop)
- you can't remove a plate from the middle or bottom directly