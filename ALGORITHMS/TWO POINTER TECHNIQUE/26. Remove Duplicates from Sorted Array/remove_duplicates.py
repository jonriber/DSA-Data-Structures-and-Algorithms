
# integer array sorted in non-decreasing order
def remove_duplicates(nums):
  if not nums:
    return 0
  
  [i, j,exclusive_number_counter] = [0, 1, 0]
  while j < len(nums):
    print("j is lower than len(nums)")
    print(f"i: {i}, j: {j}")
    if nums[i] != nums[j]:
      exclusive_number_counter += 1
      print("nums[i] is not equal to nums[j]")
      i += 1
      nums[i] = nums[j]
      print(f"i: {i}, j: {j}")
    else:
      print("nums[i] is equal to nums[j]")
      nums[j] = "-"
    j += 1
    print("J now is incremented by 1",j)
  return exclusive_number_counter, nums

if __name__ == "__main__":
  result = remove_duplicates([1, 1, 2, 2, 3])
  print(result)