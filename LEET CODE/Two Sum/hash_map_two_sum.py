
def two_sum_solution(nums, target):
  """
  Find two indices in nums such that the numbers at those indices add up to target.

  :param nums: List[int] - List of integers
  :param target: int - Target sum
  :return: List[int] - Indices of the two numbers that add up to target
  """
  hasher = {} 
  for i, number in enumerate(nums):
    print(f"Checking number: {number} at index: {i}")

    complement = target - number
    print(f"Complement needed: {complement}")
    if hasher.get(number) is not None:
      print(f"Found complement {number} in hash map at index {hasher.get(number)}")
      return [hasher.get(number), i]
    hasher[complement] = i

  

if __name__ == "__main__":
  nums = [2, 7, 11, 15]
  target = 9
  result = two_sum_solution(nums, target)
  # print(f"Indices of numbers that add up to {target}: {result}")
  print("Result:", result)


