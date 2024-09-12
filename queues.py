# First in first out, client can only add to the end of the queue or remove from the front
class Queue:
    def __init__(self, size):
        self.data = []
        for i in range(size):
            self.data.append("<EMPTY>") # Initialize the data list with "<EMPTY>"
        
        self.end = 0 # Tracks the end of the queue or next empty spot
        self.start = 0 # Tracks the front of the queue

    def enqueue(self, item):
        if self.end >= len(self.data): # Check if the queue is full
            print("Queue full!")
            return
        else:
            self.data[self.end] = item # Add the item to the end of the queue
            self.end = self.end + 1 # Increase the end by 1

    def dequeue(self):
        if self.start == self.end: # Check if the queue is empty
            print("Queue empty!")
            return
        else:
            item = self.data[self.start] # Set item variable to the first item in the queue so we can return it
            self.data[self.start] = "<EMPTY>" # Set the start to empty to remove an item
            self.start = self.start + 1 # Move the start one to the right
            return item # Return the original item 
    
    def print_q(self):
        for i in range(self.start, self.end):
            print(self.data[i])
        print(self.data, "Start:", self.start, "End: ", self.end)

if __name__ == "__main__":
    my_queue = Queue(5)

    while True:
        cmd = input("enqueue, dequeue, print, or exit? ")
        if cmd == "enqueue":
            item = input("Enter the item to push onto the stack: ")
            my_queue.enqueue(item)
        elif cmd == 'dequeue':
            value = my_queue.dequeue()
            print("dequeue() returned ", value)
        elif cmd == "print": 
            my_queue.print_q()
        elif cmd == "exit":
            break
        else:
            print("Please try again!")