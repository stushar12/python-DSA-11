class Stack:
    def __init__(self):
        self.stack = []

    def sizeStack(self):
        return len(self.stack)
	
    def isEmpty(self):
        return self.stack == []
		
    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack):
            val=self.stack[-1]
            del self.stack[-1]
            return val
        else:
            print("Stack is Empty")
    
    def peek(self):
        if len(self.stack):
            return self.stack[-1]
		
    

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Size of stack is: ",stack.sizeStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print("Peek:", stack.peek())
print("Size of stack is: ",stack.sizeStack())