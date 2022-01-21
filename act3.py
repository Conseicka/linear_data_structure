
class TwoWayNode(object):
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_song(self, song):
        
        new_song = TwoWayNode(song, None, None)
        if self.head is None:
            self.head = new_song
            self.tail = self.head
        else:
            new_song.previous = self.tail
            self.tail.next = new_song
            self.tail = new_song
        
        self.count += 1

    def reproducir(self):
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None

        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current

if __name__ == "__main__":
    theList = ["Nala", "Lisseth" , "hch", "Erick"]
    words = Queue()
    
    for data in theList:
        words.add_song(data)


    
    print(words.reproducir().data)
    print(words.reproducir().data)
    print(words.reproducir().data)
    print(words.reproducir().data)