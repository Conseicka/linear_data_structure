from random import randint
from nodeBasedQueued import Queue
from time import sleep

class Track:
    def __init__(self, title=None):
        self.title = title
        self.lenght = randint(4, 5)

class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        print(f"Count: {self.count}")

        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f"Now playing: '{current_track_node.data.title}'")

            sleep(current_track_node.data.lenght)


if __name__ == "__main__":
    musicList = ["In the end", "Somewhere I belong", "Breaking the habit", "Numb"]
    media_player = MediaPlayerQueue()
    
    for song in musicList:
        media_player.add_track(Track(song))

    media_player.play()