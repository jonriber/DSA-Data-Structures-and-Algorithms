def rob_house(nums: list[int]) -> int:
  if not nums:
    return 0
  if len(nums) <= 2:
    return max(nums)
  
  dp = [0]* len(nums)
  dp[0] = nums[0]
  dp[1] = max(nums[0], nums[1])
  
  for i in range(2, len(nums)):
    dp[i] = max(nums[i]+ dp[i-2], dp[i-1])
    
  return dp[-1]
    
    

if __name__ == '__main__':
  test1 = [1, 2, 3, 1]
  test2 = [2, 7, 9, 3, 1]
  
  result1 = rob_house(test1)
  result2 = rob_house(test2)
  
  print(f"Test 1 Result: {result1}")  # Expected output: 4
  print(f"Test 2 Result: {result2}")  # Expected output: 12