
def two_sum(nums, target):
  """_summary_
  two_sums function that finds two indices in the nums list such that the numbers at those indices add up to the target value.
  This implementation uses a two-pointer technique after sorting the list of numbers along with their original indices.
  This approach is efficient and works in O(n log n) time complexity due to sorting, followed by O(n) for the two-pointer traversal.
  Args:
    nums (_type_): _description_
    target (_type_): _description_

    
  Returns:
   
  :return: List[int] - Indices of the two numbers that add up to target
  """
  nums_with_indices = [(num, i) for i, num in enumerate(nums)]
  nums_with_indices.sort()  

  print(f"Sorted nums with indices: {nums_with_indices}")

  left, right = 0, len(nums_with_indices) - 1

  while left < right:
    current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
    if current_sum == target:
      return [nums_with_indices[left][1], nums_with_indices[right][1]]
    elif current_sum < target:
      left += 1
    else:
      right -= 1

  return []

def two_sum_no_cp(nums, target):

  num_list_with_index = [(num, i) for i,num in enumerate(nums)]
  num_list_with_index.sort()

  left, right = 0, len(num_list_with_index)-1

  while left < right:
    current_sum = num_list_with_index[left][0] + num_list_with_index[right][0]
    if current_sum == target:
      return [num_list_with_index[left][1], num_list_with_index[right][1]]
    elif current_sum <target:
      left = left + 1
    else:
      right -= 1

  return None



if __name__ == "__main__":
  
  nums = [2, 7, 11, 15]
  target = 9
  result = two_sum(nums, target)
  print(f"Indices of numbers that add up to {target}: {result}")

  nums2 = [11, 15, 2, 7]
  target2 = 10
  result2 = two_sum_no_cp(nums2, target2)
  print(f"Indices of numbers that add up to {target2}: {result2}")

