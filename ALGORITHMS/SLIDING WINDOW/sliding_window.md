# Sliding window technique

The sliding window technique is a powerful algorithmic approach used to solve problems that involve analyzing a subset
of a sequence (such as an array or string) to optimize computation. It is particularly useful for problems involving
contiguous subarrays or substrings.

## Core concept

- A window is a subset of the input data that moves (or "slides") through the data structure.
- The window typically has a fixed size or is allowed to expand and shrink dynamically depending on the problem.
- Instead of recomputing the properties of the window from scratch every time it moves, the sliding window technique
incrementally updates the computation.

```This approach reduces the time complexity from 
𝑂(𝑛⋅𝑘)
O(n⋅k) (recomputing for each window) to 
𝑂(𝑛)
O(n) in many scenarios.

```

## Key Steps in the Sliding Window Technique

- Initialize a window: Define the start and end of the window (often two pointers).
- Expand the window: Move the end of the window forward to include new elements.
- Shrink the window (if necessary): Move the start of the window forward to exclude elements that are no longer needed.
- Update results: After adjusting the window, update the desired result (e.g., maximum, minimum, sum, etc.).
- Repeat until the window has traversed the entire data structure.

## When to Use Sliding Window

The sliding window is most effective for problems involving:

- Contiguous subarrays or substrings (e.g., finding maximum/minimum sums, longest substring).
- Problems where the size of the window is fixed or dynamically adjusted based on certain conditions.

## Why Sliding Window is Efficient

- Incremental Updates: Instead of recalculating the sum of a subarray from scratch, only the changes at the boundaries 
of the window are considered.
- Single Pass: The window "slides" through the data, requiring only one pass (linear traversal) to compute the result.

This optimization is crucial in reducing time complexity, especially when working with large datasets.

## Common Problems Using Sliding Window

- Fixed-size window problems:
  - Maximum/Minimum sum of a subarray of size 𝐾
  - Find average of all contiguous subarrays of size 𝐾
- Variable-size window problems:
  - Longest substring with 𝐾K unique characters.
  - Smallest subarray with a sum greater than 𝑆S.
- Two-pointer variations:
  - Longest subarray with at most 𝐾K distinct integers.
  - Longest substring without repeating characters.
