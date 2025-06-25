class ListNode:
    
  def __init__(self,val=0, next=None):
    self.val = val
    self.next = next

def reverse_linked_list_recursive(head:ListNode) -> ListNode:
  if not head or not head.next:
    return head
  new head = reverse_linked_list_recursive(head.next)
  head.next.next = head  # Reverse the link
  head.next = None  # Set the next of the current node to None
  return new_head  # Return the new head of the reversed linked list

def reverse_linked_list(head:ListNode) -> ListNode:
  """
  Reverses a singly linked list.
  
  :param head: The head of the linked list to be reversed.
  :return: The new head of the reversed linked list.
  """
  prev = None
  current = head
  
  while current:
    next_node = current.next  # Store the next node
    current.next = prev       # Reverse the link
    prev = current            # Move prev to current
    current = next_node       # Move to the next node
    
  return prev  # New head of the reversed linked list
  

if __name__ == "__main__":
  
  head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
  head2 = ListNode(1, ListNode(2))
  head3 = ListNode(1)
  head4 = None
  head5 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
  
  result1 = reverse_linked_list(head1)
  result2 = reverse_linked_list(head2)
  result3 = reverse_linked_list(head3)
  # result4 = reverse_linked_list(head4)
  result5 = reverse_linked_list(head5)
  
  # Print the results
  def print_linked_list(head):
    current = head
    while current:
      print(current.val, end=" -> ")
      current = current.next
    print("None")
  