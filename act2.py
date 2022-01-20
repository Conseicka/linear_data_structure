from linkedList import SinglyLinkedList
from array import Array


words = SinglyLinkedList()


theList = ["Nala", "Lisseth" , "hch", "Erick"]
theArray = Array(len(theList))

for index in range(len(theList)):
    theArray.__setitem__(index, theList[index])


for data in theArray:
    words.append(data)

#for word in words.iter():
 #   print(word)


words.search("Lisseth")
head = words.scan("a")
print(head)

print(words.replace_item("Erick", "David").data)

print("-----"* 20)

words.append("Green Day")

words.insert_new_head("Zack")

words.remove_node("hch")

words.insert_node_before("Nala","Metarraluciano")

words.insert_node_after("David", "Python")

#words.delete_by_index(3)

counter = 0
for word in words.iter():
    print(word)
    counter += 1

print("-----"* 20)

words.insert_node_by_index(2,"Leona")

counter = 0
for word in words.iter():
    print(word)
    counter += 1