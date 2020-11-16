class Cell:

    def __init__(self, contents = None):
        self.contents = contents


class Row:

    def __init__(self, num_of_cells = 0, is_header = False):
        self.is_header = is_header
        self.cells = []
        for _ in range(num_of_cells):
            self.cells.append(Cell())
    

class Table:

    def __init__(self, num_of_rows = 0, cells_per_row = 0, has_header = True):
        self.rows = []
        for i in range(num_of_rows):
            if i == 0 and has_header:
                self.rows.append(Row(cells_per_row, is_header=True))
            else:
                self.rows.append(Row(cells_per_row))
    
    @staticmethod
    def matrixToTable(matrix = [[]], has_header = False):
        table = Table()
        for i in range(len(matrix)):
            if i == 0 and has_header:
                row = Row(is_header = True)
            else:
                row = Row()
            for elem in matrix[i]:
                row.cells.append(Cell(elem))
            table.rows.append(row)
        return table
        

