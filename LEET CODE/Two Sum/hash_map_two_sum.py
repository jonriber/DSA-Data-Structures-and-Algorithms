
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
    if complement not in hasher:
      hasher[number] = i
    print(f"Hash map after processing: {hasher}")

    return [hasher.get(complement), i]
  print("Testing for complement in hash map", hasher.get(2))

  

if __name__ == "__main__":
  nums = [2, 7, 11, 15]
  target = 9
  result = two_sum_solution(nums, target)
  # print(f"Indices of numbers that add up to {target}: {result}")
  print("Result:", result)


