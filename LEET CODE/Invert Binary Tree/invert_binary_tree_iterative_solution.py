from collections import deque

def invert_tree(node):
  if not node:
    return None
  
  queue = deque([node])
  print("initial queue:", queue)
  

if __name__ == "__main__":
  pass