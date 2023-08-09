#Think how to add/apply is_FULL??

class Stack:
    def __init__(self): #constructer to make stack ready
        self.items = []

    def is_empty(self): #to cheack stack has no item
        return len(self.items) == 0

    def push(self, item): #to add at the end
        self.items.append(item)

    def pop(self):
        if not self.is_empty(): #remove at the end
            return self.items.pop()
        else:
            raise IndexError("Stack is empty, cannot pop an item.")#exception handling

    def peek(self): #accessing last element
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty, cannot peek an item.")

    def size(self):
        return len(self.items)
    
    