# Detect a cycle in a linked list

class ListNode:
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next
    
def has_cycle(head):
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False

if (__name__ == '__main__'):
  node1 = ListNode(1)
  node2 = ListNode(2)
  node3 = ListNode(3)
  node1.next = node2
  node2.next = node3
  node3.next = node1  # Creates a cycle

  print(has_cycle(node1))