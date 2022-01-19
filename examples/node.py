


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


if __name__ == "__main__":
  
    head = None
    for count in range (1,5):
        head = Node(count, head)
    
    while head != None:
        print(head.data)
        head = head.next
