class Cell:

    def __init__(self, contents = None):
        self.contents = contents


class Row:

    def __init__(self, num_of_cells = 0):
        self.cells = []
        for _ in range(num_of_cells):
            self.cells.append(Cell())
    

class Table:

    def __init__(self, num_of_rows = 0, cells_per_row = 0):
        self.rows = []
        for _ in range(num_of_rows):
            self.rows.append(Row(cells_per_row))

