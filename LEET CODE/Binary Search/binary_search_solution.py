def binary_search(nums, target):
  left_pointer, right_pointer = 0, len(nums) -1
  
  while left_pointer <= right_pointer:
    mid = (left_pointer + right_pointer) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      left_pointer = mid +1
    else:
      right_pointer = mid -1
      
  return -1
    
if __name__ == "__main__":
  nums1= [-1,0,3,5,9,12]
  target1 = 9
  nums2 = [-1,0,3,5,9,12]
  target2 = 2
  
  