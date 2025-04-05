
def rot_left(a,d):
  # Write your code here
  print("a",a)
  print("d",d)
  if (len(a) <1 | d <1):
      return a
  real_rotations = d%len(a)
  result = a[real_rotations:] + a[:real_rotations]
  print("test 1:",a[:real_rotations])
  print("test 2:",a[real_rotations:])
  print("real rotaions:",real_rotations)
  print("Result:",result)
  return result

if __name__ == '__main__':
  test_array = [1, 2, 3, 4, 5]
  number_of_rotations = 4
  # print("first:", test_array[2:])
  # print("second:", test_array[:2])
  # print("result:", test_array[2:] + test_array[:2])
  rot_left(test_array, number_of_rotations)
  print("Expected: [5, 1, 2, 3, 4]")
  print("Actual:", rot_left(test_array, number_of_rotations))