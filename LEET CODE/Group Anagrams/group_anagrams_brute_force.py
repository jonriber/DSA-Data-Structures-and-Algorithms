from collections import defaultdict


def group_anagrams(strs):
  """_summary_

  Args:
      strs (_type_): _description_
  """
  anagrams = defaultdict(list)

  for word in strs:
    print(f"Processing word: {word}")

    sorted_word = tuple(sorted(word))

    print(f"Sorted word: {sorted_word}")

    anagrams[sorted_word].append(word)

    print(f"Anagrams grouped: {anagrams}")

  # return list(anagrams.keys())
  return list(anagrams.values())
  

if __name__ == "__main__":
  strs = ["eat","tea","tan","ate","nat","bat"]
  result = group_anagrams(strs)
  print(f"Grouped anagrams: {result}")