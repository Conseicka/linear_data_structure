from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def __scan_before(self, data):
        head = self.tail
        while head != None and data != head.data:
            probe = head
            head = head.next
        return probe, head

    def append(self, data):
        node = Node(data)

        if self.tail == None:
            self.tail = node

        else:
            current = self.tail

            while current.next:
                current = current.next

            current.next = node

        self.size += 1


    def make_circ(self):
        head = self.tail
        while head != None:
            probe = head
            head = head.next
        probe.next = self.tail


    def size(self):
        return str(self.size)


    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val
        

    def search(self, target_item):
        head = self.tail
        while head != None and target_item != head.data:
            head = head.next
       
        if head is not None:
            print(f"Data {target_item} found!")        
        else:
            print(f"Target item '{target_item}' is not in the linked list")

        return head

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0


    def scan(self, target_item):
        head = self.tail
        while head != None and target_item != head.data:
            head = head.next
 
        return head

    def replace_item(self, target_item, new_value):
        current = self.scan(target_item)
        if current is not None:
            current.data = new_value
        
        return current

    def insert_new_head(self, new_value):
        try:
            self.tail = Node(new_value, self.tail)
            self.size += 1
        except:
            return None
    


    def insert_node_before(self, index_node, insert_node):
        probe, head = self.__scan_before(index_node)
        try:
            new_node = Node(insert_node,probe.next)
            probe.next = new_node
            self.size += 1
        except:
            return None
    
    def insert_node_after(self, index_node, insert_node):
        head = self.scan(index_node)
        new_node = Node(insert_node, head.next)
        head.next = new_node
        self.size += 1

    def insert_node_by_index(self, index, data):
        head = self.tail
        probe = None
        while index > 1 and head.next.next != None:
            head = head.next
            index -= 1
        new_node = Node(data,head.next.next)
        head.next = new_node

    def remove_node(self, delet_node):
        probe, head = self.__scan_before(delet_node)
        try:
            probe.next = head.next
            self.size -= 1
        except:
            return None

    def delet_by_data(self, data):
        current = self.tail
        previous = self.tail

        while current.data:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data

            previous = currentcurrent = current.next
    
    def delete_by_index(self, delete_inex):
        head = self.tail
        if delete_inex <= 0 or head.next is None:
            removed_item = head.data
            print(f"The item {removed_item} was removed")
        else: 
            probe = head
            while delete_inex > 1 and probe.next.next != None:
                probe = probe.next
                delete_inex -= 1
        removed_item = probe.next.data
        probe.next = probe.next.next
        print(f"the item {removed_item} was removed")


    if __name__ == "__main__":
        pass