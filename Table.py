class Cell:

    def __init__(self, contents):
        self.contents = contents


class Row:

    def __init__(self, length = 0):
        self.length = length
    

class Table:

    def __init__(self, num_of_rows = 0, cells_per_row = 0):
        self.table = []
        for _ in range(num_of_rows):
            self.table.append(Row(cells_per_row))


