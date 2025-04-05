
def hourglassSum(arr):
  max_sum = -63 # minimum value of sum of hourglass is -9 * 7 = -63
  for i in range(4):
    for j in range(4):
      top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
      middle = arr[i+1][j+1]
      bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
      
      sum_hourglass = top + middle + bottom
      if sum_hourglass > max_sum:
        max_sum = sum_hourglass
  return max_sum
 
if __name__ == '__main__':
  pass