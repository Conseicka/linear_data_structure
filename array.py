from functools import reduce

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __replace__(self, index, new_element):
        self.items[index] = new_element

    def __sum_array__(self):
        items = self.items
        try:
            sum_array = reduce(lambda a, b: a + b, self.items)

        except:
            items = int(items)
            sum_array = reduce(lambda a, b: a + b, self.items)
        return sum_array


if __name__ == "__main__":
    vector = Array(5)
    print(vector.__str__())