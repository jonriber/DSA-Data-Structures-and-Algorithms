from collections import defaultdict

def group_anagrams(list_words):
  anagrams = defaultdict(list)

  for word in list_words:
    count = [0] * 26
    for char in word:
      count[ord(char) - ord('a')] += 1

    anagrams[tuple(count)].append(word)

  return list(anagrams.values())  

if __name__ == "__main__":
  
  test_sample = ["eat", "tea", "tan", "ate", "nat", "bat"]
  result = group_anagrams(test_sample)
  print(f"Grouped anagrams: {result}")