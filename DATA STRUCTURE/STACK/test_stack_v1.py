import unittest
from stack_v1 import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 'Stack is empty')

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 'Stack is empty')
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

if __name__ == '__main__':
    unittest.main()