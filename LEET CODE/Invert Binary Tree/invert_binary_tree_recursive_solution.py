class TreeNode:
  def __init__(self, val=0, left= None, rigth=None):
    self.val = val
    self.left = left
    self.right = rigth

def invert_binary_tree(root: TreeNode) -> TreeNode:
  if root is None:
    return None
  
  root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
  return root

if __name__ == "__main__":
  root1 = TreeNode(4)
  root1.left = TreeNode(2)
  root1.right = TreeNode(7)
  root1.left.left = TreeNode(1)
  root1.left.right = TreeNode(3)
  root1.right.left = TreeNode(6)
  root1.right.right = TreeNode(9)
  inverted_tree1 = invert_binary_tree(root1)
  print(inverted_tree1.val)  # Output: 4
  print(inverted_tree1.left.val)  # Output: 7
  print(inverted_tree1.right.val)  # Output: 2
  print(inverted_tree1.left.left.val)  # Output: 9
  print(inverted_tree1.left.right.val)  # Output: 6
  print(inverted_tree1.right.left.val)  # Output: 3
  print(inverted_tree1.right.right.val)  # Output: 1
  