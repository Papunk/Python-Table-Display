class Cell:
    '''
    Desc:
        A single unit within a Table; contains a value
    '''

    def __init__(self, contents = None):
        self.contents = contents


class Row:
    '''
    Desc:
        A collection of Cell objects within a Table
    '''

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
    '''
    Desc:
        A collection Row objects
    '''

    def __init__(self, num_of_rows = 0, cells_per_row = 0, has_header = True):
        self.rows = []
        for i in range(num_of_rows):
            if i == 0 and has_header:
                self.rows.append(Row(cells_per_row, is_header=True))
            else:
                self.rows.append(Row(cells_per_row))
    
    def longestElement(self) -> int:
        '''
        Desc:
            Returns the length of the element with the longest string representation
        '''
        longest = 0
        for row in self.rows:
            for cell in row.cells:
                if len(str(cell.contents)) > longest:
                    longest = len(str(cell.contents))
        return longest

    @staticmethod
    def matrixToTable(matrix = [[]], has_header = False):
        '''
        Desc:
            Returns a Table from a 2D array
        
        Parameters:
            matrix - a 2D array containing the values of the cells for the Table
            has_header - determines wether the Table will have a header
        '''
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

    
    def asMatrix(self):
        '''
        Desc:
        Turns the internal table as a 2D array
        '''
        matrix = []
        for row in self.rows:
            lst = []
            for cell in row.cells:
                lst.append(cell.contents)
            matrix.append(lst)
        return matrix

        

