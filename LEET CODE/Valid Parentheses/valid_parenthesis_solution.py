
def valid_parenthesis(s:str) -> bool:
  """
    @param s: str - input string containing only '(', ')', '{', '}', '[' and ']'
    @return: bool - True if the input string is valid, False otherwise
  """
  stack = []
  bracket_mapping = {
    ')': '(',
    '}': '{',
    ']': '['
  }

  for char in s:
    print(f"Processing character: {char}")
    if char in bracket_mapping.values():
      print(f"Checking values: {bracket_mapping.values()} and condition: {char in bracket_mapping.values()}")
      stack.append(char)
    elif char in bracket_mapping:
      print(f"Checking keys: {bracket_mapping.keys()} and condition: {char in bracket_mapping}")
      if not stack or stack[-1] != bracket_mapping[char]:
        return False
      stack.pop()
    else:
      return False
  return not stack

if __name__ == "__main__":
  test_string1 = "({[]})"
  test_string2 = "({[})"
  print(valid_parenthesis(test_string1))  # Expected output: True
  print(valid_parenthesis(test_string2))  # Expected output: False
  print(valid_parenthesis("()"))  # Expected output: True

