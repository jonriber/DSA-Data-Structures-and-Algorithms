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
  
def group_anagram_no_cp(words):

  anagrams = defaultdict(list)

  print(f"Anagrams: {anagrams}")

  for word in words:

    print("The word is: ", word)

    sorted_word = sorted(word)
    print(f"Sorted word: {sorted_word}")

    tuple_sorted_word = tuple(sorted_word)
    print(f"Tuple sorted word: {tuple_sorted_word}")

    anagrams[tuple_sorted_word].append(word)
    print(f"Anagrams grouped: {anagrams}")

  print(f"Anagrams grouped: {anagrams}")

  print(f"Anagrams grouped values: {anagrams.values()}")

  print(f"Anagrams grouped keys: {anagrams.keys()}")

  print(f"Anagrams grouped items: {anagrams.items()}")

  print(f"Anagrams grouped as list: {list(anagrams.values())}")

  return list(anagrams.values())

if __name__ == "__main__":
  strs = ["eat","tea","tan","ate","nat","bat"]
  # result = group_anagrams(strs)
  result2 = group_anagram_no_cp(strs)
  # print(f"Grouped anagrams: {result}")