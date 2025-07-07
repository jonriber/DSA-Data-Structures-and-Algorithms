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
  pass