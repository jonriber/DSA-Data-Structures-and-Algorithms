def two_strings(s1, s2):
# Write your code here
  dict_s1 = dict()
  # print("s1:",s1)
  # print("s2:",s2)
  for i in s1:
      # print("i in word 1:",i)
      if i not in dict_s1:
          dict_s1[i] = 1
      else:
          dict_s1[i] += 1
  for j in s2:
      if j not in dict_s1:
          print("NO")
          # return "NO"
          continue
      else:
          # if dict_s1[j] >0:
          #     dict_s1[j] -= 1
          #     continue
          #     return "YES"
          # else:
          #     print("NO")
          #     # return "NO"
          #     continue
          return "YES"
  
  print("dictionary:",dict_s1)

  return "NO"

if '__init__' == '__main__':
  two_strings("hello", "world")
  two_strings("hi", "world")