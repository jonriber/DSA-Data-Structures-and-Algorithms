
def check_magazine(magazine, note):
  # Write your code here
  # print("magazine:", magazine)
  # print("note:",note)
  magazine_dict = {}
  for i in magazine:
      # print("item:",i) 
      if  i not in magazine_dict:
          # print("entered here")
          magazine_dict[i] = 1
      else:
          magazine_dict[i] += 1
  for word in note:
      if word not in magazine_dict:
          # print("Word not in magazine dict:", word)
          print("No")
          return
      else:
          if magazine_dict[word] > 0:
              magazine_dict[word] -= 1
              continue
          else:
              print("No")
              return
  print("Yes")
  # print("magazine_dict",magazine_dict)

if '__init__' == '__main__':
  # pass
  magazine = "give me one grand today night".rstrip().split()
  note = "give one grand today".rstrip().split()
  check_magazine(magazine, note)
  magazine = "two times three is not four".rstrip().split()
  note = "two times two is four".rstrip().split()
  check_magazine(magazine, note)