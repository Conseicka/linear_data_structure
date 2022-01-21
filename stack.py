from array import Array
from node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.bottom_node = None

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
    
        else:
            self.top = node
            self.bottom_node = node
        
        self.size += 1

    
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next

            else:
                self.top = None
            
            return data
        
        else:
            return "Tne stack is empty"
    

    def peek(self):
        if self.top:
            return self.top

        else:
            return "The stack is empty"


    def clear(self):
        while self.top:
            self.pop()

    def iter(self):
        current = self.peek()
        
        while current:
            val = current.data
            current = current.next
            yield val

    def bottom(self):
        return self.bottom_node

    
    def scan(self, target_data):
        current = self.peek()
       
        while current != None and target_data != current.data:
            current = current.next
        
        return current
    
 


if __name__ == "__main__":

    theList = ["Nala", "Lisseth" , "hch", "Erick"]
    words = Stack()
    
    for data in theList:
        words.push(data)


    for word in words.iter():
        print(word)