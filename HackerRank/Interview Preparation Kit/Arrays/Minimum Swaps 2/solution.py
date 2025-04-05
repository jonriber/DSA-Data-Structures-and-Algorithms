def minimumSwaps(arr):
  total_swaps = 0
  n = len(arr)
  visited = [False] * n
  
  for i in range(n):
    if visited[i] or arr[i] == i +1:
      print(" second condition", arr[i], i, i+1)
      continue
    cycle_length = 0
    x = i
    while not visited[x]:
      visited[x] = True
    

if __name__ == "__main__":
  pass