
def climb_stairs(n: int) -> int:
  """
    arg: n (int): The total number of steps to climb.
    return: int: The number of distinct ways to climb to the top.
    
    This function calculates the number of distinct ways to climb a staircase with n steps,
    where you can take either 1 or 2 steps at a time. It uses dynamic programming to build up
    the solution iteratively.
  """
  if n == 0 or n == 1:
    return 1
  
  a, b = 1, 1

  for i in range(2, n+1):
    a,b = b, a+b

  return b

if __name__ == '__main__':
  example_input = 5
  result = climb_stairs(example_input)
  print(f"The number of distinct ways to climb {example_input} steps is: {result}")
  