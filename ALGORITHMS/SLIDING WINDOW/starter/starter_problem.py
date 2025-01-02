def max_sum_subarray(arr, K):
    max_sum = 0
    window_sum = sum(arr[:K])
    max_sum = window_sum
    
    for i in range(len(arr) - K):
        window_sum = window_sum - arr[i] + arr[i + K]
        max_sum = max(max_sum, window_sum)
        
    return max_sum
    


if (__name__ == '__main__'):
    # pass
    # Write
    
    # Test cases
  print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Expected: 9
  print(max_sum_subarray([2, 3, 4, 1, 5], 2))     # Expected: 7