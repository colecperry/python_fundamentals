# LIFO - Last in, first out. Can only add, remove, examine
class Stack:
    def __init__(self, size):
        self.data = []
        for i in range(size):
            self.data.append(0) # Initialize the data list with all zeros
        self.end = 0 # Tracks the number of elements in the stack
    
    def push(self, item):
        if self.end >= len(self.data): # Check if the stack is full
            print("Stack full!")
            return # Return without modifying the stack
        else:
            self.data[self.end] = item # Set the item to the "self.end" index in the list, which is the next open zero
            self.end = self.end + 1 # Increase the size of the stack
    
    def pop(self):
        if self.end <= 0: # Check if the stack is empty
            print("Stack empty!")
            return # Return without modifying the list
        else:
            self.end = self.end - 1 
            return self.data[self.end] # Return the popped item
    
    def print_stack(self):
        for i in range(self.end - 1, -1, -1): # Start at self.end - 1 b/c self.end is pointed at the first zero in the list
            print(self.data[i])

# Note on the pop method - if your list is [1,2,3,0,0], and you run pop, it will decrement from 3 to 2, but it will leave 3 unchanged until you push something back onto the stack

if __name__ == "__main__":
    my_stack = Stack(6)

    while True:
        cmd = input("push, pop, print, or exit? ")
        if cmd == "push":
            value = input("Enter the item to push onto the stack: ")
            my_stack.push(value)
        elif cmd == 'pop':
            value = my_stack.pop()
            print("pop() returned ", value)
        elif cmd == "print": 
            my_stack.print_stack()
        elif cmd == "exit":
            break
        else:
            print("Please try again!")
