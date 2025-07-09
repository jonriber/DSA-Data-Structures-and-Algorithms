def can_jump(nums):
  
  max_reach = 0
  
  for i, jump in enumerate(nums):
    if i > max_reach:
      return False
    max_reach = max(max_reach, i + jump)
  return True

if __name__ == "__main__":
  
  nums = [2, 3, 1, 1, 4]
  print("Input:", nums)
  result = can_jump(nums)
  print("Output:", result)
  
  # Example usage
  nums2 = [3, 2, 1, 0, 4]
  print("Input:", nums2)
  result2 = can_jump(nums2)
  print("Output:", result2)
  
  

