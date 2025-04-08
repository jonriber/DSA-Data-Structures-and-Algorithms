# Bubble Sort

The following version of Bubble Sort 

```python

for (int i = 0; i < n; i++) {
    
  for (int j = 0; j < n - 1; j++) {
    // Swap adjacent elements if they are in decreasing order
    if (a[j] > a[j + 1]) {
        swap(a[j], a[j + 1]);
    }
  }
}
```

If given an array of integers, I need to sort this array in ascending order using the Bubble Sort algorithm.

Once my array is sorted, I should print the following three lines:

1. Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
2. First Element: firstElement, where  is the first element in the sorted array.
3. Last Element: lastElement, where  is the last element in the sorted array.

## Solution

On the above code snippet, the swap function is not a native python method. In order to execute that, I have used
a temporary variable to hold value and swap elements based on their array index.

Also, It is important to have two iterations through the array, the outer one, with a flag called swapped.
This flag is set to true every time a swap happens, which means the whole array iteration should happen again.