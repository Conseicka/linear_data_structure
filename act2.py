from linkedList import SinglyLinkedList
from array import Array

theList = ["Nala", "Lisseth" , "hch", "Erick"]
theArray = Array(len(theList))

for index in range(len(theList)):
    theArray.__setitem__(index, theList[index])


words = SinglyLinkedList()

for data in theArray:
    words.append(data)

for word in words.iter():
    print(word)
