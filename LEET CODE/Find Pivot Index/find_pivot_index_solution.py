
def find_pivot_index(nums):
  total = sum(nums)
  left_sum = 0
  for i,n in enumerate(nums):
    print(f"Index: {i}, number: {n}")
    if left_sum == (total- n -  left_sum):
      print(f"Pivot found at index: {i}")
      return i
    print(f"Pivot not found yet at index: {i}, addin {n} to left_sum")
    left_sum += n
  print("No pivot index found")
  return -1

if __name__ == '__main__':
  # Example usage
  nums = [1, 7, 3, 6, 5, 6]
  print(find_pivot_index(nums))  # Output: 3

  # second example
  nums = [1, 2, 3]
  print(find_pivot_index(nums))  # Output: -1

  # third example
  nums = [2, 1, -1]
  print(find_pivot_index(nums))  # Output: 0
  # fourth example
  nums = [1, 2, 3, 4, 5]
  print(find_pivot_index(nums))  # Output: -1
  # fifth example
  nums = [1, 2, 3, 4, 5, 6]
  print(find_pivot_index(nums))  # Output: -1
  # sixth example
  nums = [1, 2, 3, 4, 5, 6, 7]
  print(find_pivot_index(nums))  # Output: -1
  # seventh example
  nums = [1, 2, 3, 4, 5, 6, 7, 8]
  print(find_pivot_index(nums))  # Output: -1
  # eighth example
  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(find_pivot_index(nums))  # Output: -1
  # ninth example
  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print(find_pivot_index(nums))  # Output: -1
  # tenth example
  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  print(find_pivot_index(nums))  # Output: -1