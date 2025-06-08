
def two_sum(nums, target):
  """_summary_

  Args:
      nums (_type_): _description_
      target (_type_): _description_
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

  return []  # Return an empty list if no solution is found



if __name__ == "__main__":
  
  nums = [2, 7, 11, 15]
  target = 9
  result = two_sum(nums, target)
  print(f"Indices of numbers that add up to {target}: {result}")

  nums2 = [11, 15, 2, 7]
  target2 = 9
  result2 = two_sum(nums2, target2)
  print(f"Indices of numbers that add up to {target2}: {result2}")

