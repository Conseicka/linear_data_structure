from array import Array


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
 
class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous
        self.tail = None
        self.size = 0
        
    
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):      
        node = TwoWayNode(data)
        probe = None

        if self.tail == None:
            self.tail = node
            
        else:     
            current = self.tail

            while current.next:
                probe = current
                current = current.next
      
            current.previous = probe
            node.previous = current
            current.next = node  

        self.size += 1


    def size(self):
        return str(self.size)


    def iter(self):
        current = self.tail
        while current:           
            val = current.data
            current = current.next
            yield val

    def iter_reverse(self):
        for node in self.iter():
            last_node = node

        current = self.scan(last_node)
        while current:           
            val = current.data
            current = current.previous
            yield val

    def scan(self, target_item):
        head = self.tail
        while head != None and target_item != head.data:
            head = head.next
 
        return head


    def search(self, target_item):
        head = self.tail

        while head != None and target_item != head.data:
            head = head.next
 
        if head is not None:
            print(f"Data {target_item} found!")        
        else:
            print(f"Target item '{target_item}' is not in the linked list")

        return head
    
    def insert_new_head(self, data):
        head = self.tail
        try:
            self.tail = TwoWayNode(data, None, self.tail)
            head.previous = self.tail
            self.size += 1
        except:
            return None
        print(self.tail.next.data)


    def replace_item(self, new_value, current_value):
        current = self.scan(current_value)
        if current is not None:
            current.data = new_value

        return current


    def insert_node_before(self, new_value, target_value):
        current = self.scan(target_value)
       
        if current is not None:
            new_node = TwoWayNode(new_value, current.previous, current)
            current.previous.next = new_node
            
            self.size += 1
            return new_node

        return current


    def insert_node_after(self, new_value, target_value):
        current = self.scan(target_value)
        
        if current is not None:
            new_node = TwoWayNode(new_value, current, current.next)            
            current.next.previous = new_node
            current.next = new_node

            self.size += 1
            return new_node

        return current


    def insert_node_by_index(self, index, new_value):
        try:
            for data in self.iter():
                index -= 1
            
            new_node = self.insert_node_before(new_value,data)
        except:
            return None
        
        self.size += 1
        return new_node


    def delete_node_by_data(self, data):
        try:
            target_data = self.scan(data)
            target_data.previous.next = target_data.next
            target_data.next.previous = target_data.previous
        except:
            return None

        self.size -= 1
        return target_data

    def delete_by_index(self, index):
        try:
            for data in self.iter():
                index -= 1
                
            target_data = self.scan(data)
            target_data.previous.next = target_data.next
            target_data.next.previous = target_data.previous

        except:
            return None

        self.size -= 1
        return target_data


if __name__ == "__main__":
    words = TwoWayNode(None)
    


    theList = ["Nala", "Lisseth" , "hch", "Erick"]
    theArray = Array(len(theList))

    for index in range(len(theList)):
        theArray.__setitem__(index, theList[index])

 
    for data in theArray:
          words.append(data)



    for word in words.iter():
        print("word",word)

    #words.delete_by_index(1)
    print("----"*20)

    for word in words.iter_reverse():
       print("word",word)