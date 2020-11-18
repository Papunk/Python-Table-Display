class Cell:

    def __init__(self, contents = None):
        self.contents = contents


class Row:

    def __init__(self, num_of_cells = 0, is_header = False):
        self.is_header = is_header
        self.cells = []
        for _ in range(num_of_cells):
            self.cells.append(Cell())

    @ staticmethod
    def listToRow(lst = [], is_header = False):
        row = Row()
        row.is_header = is_header
        for elem in lst:
            row.cells.append(elem)
        return row
    

class Table:

    def __init__(self, num_of_rows = 0, cells_per_row = 0, has_header = True):
        self.rows = []
        for i in range(num_of_rows):
            if i == 0 and has_header:
                self.rows.append(Row(cells_per_row, is_header=True))
            else:
                self.rows.append(Row(cells_per_row))
    
    def longestElement(self) -> int:
        longest = 0
        for row in self.rows:
            for cell in row.cells:
                if len(str(cell.contents)) > longest:
                    longest = len(str(cell.contents))
        return longest

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
        

