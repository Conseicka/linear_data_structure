from array import Array


class Grid(object):
    """Represents a two-dimensional array."""
    def __init__(self, rows, columns, fill_value = None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        "Returns the number of rows."
        return len(self.data)

    def get_width(self):
        """Returns the number of columns."""
        return len(self.data[0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [row][column]."""
        return self.data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"

        return str(result)

class Cube(Grid):
    def __init__(self,rows ,cols ,depth ,fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(cols)
            for col in range(cols):
                self.data[row][col] = Array(depth, fill_value)
    
    def get_depth(self):
        return len(self.data[0][0])

    def to_str(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][col][depth]) + " "
                
                result += "\n"
        return str(result)

if __name__ == "__main__":
    matrix = Cube(3,4,5)
    print(matrix.get_height())
    print(matrix.get_width())
    print(matrix.get_depth())
    print(matrix.to_str())
