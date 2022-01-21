class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack.pop()

if __name__ == "__main__":
    theList = [1, 2 , 3, 4]
    words = Queue()
    
    for data in theList:
        words.enqueue(data)


    print(words.dequeue(),"enqueue")
    