
class Stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return not bool(self.stack)
    
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.stack[-1]
    
if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    print(stack.pop())
    print(stack.peek())
    stack.push(1)
    stack.push(2)
    print(stack.peek())
    stack.push(3)
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())