

class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0 ,data)
        self.size += 1


    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        total_items = range(self.size)

        for item in total_items:
            print(self.items[item])


if __name__ == "__main__":
    theList = ["Nala", "Lisseth" , "hch", "Erick"]
    words = Queue()
    
    for data in theList:
        words.enqueue(data)


    print(words.dequeue(),"enqueue")
    words.traverse()