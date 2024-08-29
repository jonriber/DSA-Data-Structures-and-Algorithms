
# integer array sorted in non-decreasing order
def remove_duplicates(nums):
  [i, j] = [0, 1]
  while j < len(nums):
    print("j is lower than len(nums)")
    print(f"i: {i}, j: {j}")
    if nums[i] != nums[j]:
      print("nums[i] is not equal to nums[j]")
      i += 1
      nums[i] = nums[j]
      print(f"i: {i}, j: {j}")
    j += 1
    print("J now is incremented by 1",j)

if __name__ == "__main__":
  remove_duplicates([1, 1, 2, 2, 3]) # 2