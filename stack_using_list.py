# LIFO - Last in, first out. Can only add, remove, examine
class Stack:
    def __init__(self, size):
        self.data = list() # add an empty list to store data
        self.size = size # Size is optional
    
    def push(self, item):
        if len(self.data) >= self.size: # Check if the stack is full
            print("Stack full!")
            return # Return without modifying the stack
        else:
            self.data.append(item) # Append returns no value in python
    
    def pop(self):
        if self.size <= 0: # Check if the stack is empty
            print("Stack empty!")
            return # Return without modifying the list
        else:
            return self.data.pop() # Pop removes and returns last item
    
    def print_stack(self):
        for i in range(len(self.data) - 1, -1, -1): # Start at self.end - 1 b/c self.end is pointed at the first zero in the list
            print(self.data[i])

    def peek(self):
        return self.data[len(self.data)-1]

# Note on the pop method - if your list is [1,2,3,0,0], and you run pop, it will decrement from 3 to 2, but it will leave 3 unchanged until you push something back onto the stack

if __name__ == "__main__":
    my_stack = Stack(6)

    while True:
        cmd = input("push, pop, print, peek, or exit? ")
        if cmd == "push":
            value = input("Enter the item to push onto the stack: ")
            my_stack.push(value)
        elif cmd == 'pop':
            value = my_stack.pop()
            print("pop() returned ", value)
        elif cmd == "print": 
            my_stack.print_stack()
        elif cmd == 'peek':
            print(my_stack.peek())
        elif cmd == "exit":
            break
        else:
            print("Please try again!")