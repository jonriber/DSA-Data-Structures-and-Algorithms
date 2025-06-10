# Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

## LINK:

<https://leetcode.com/problems/group-anagrams/description/>

## Solutions 

### First: Sorting with dictionaries and lists

On this solution, we start by creating a new `defaultdict` and an empty list inside.

After that, it is time to iterate through the array of words.

For each `word`, and for each `character` of the word, we sort it and create a tuple (immutable).

Once we have this sorted tuple, it will become a key of the first dictionary.

The idea is to store a list of `words` for the equivalent keys of the dictionary.

#### Time complexity

- Sorting each word takes O(k log k), where k is the length of the word.
- If there are n words, the total time complexity is O(n * k log k).

### Second: No sorting and dictionaries and lists