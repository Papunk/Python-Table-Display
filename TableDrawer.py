from Table import *
from enum import Enum

# Some values:

ASTERISK = '*'
HASH = '#'
LINE = '|'
F_SLASH = '/'
B_SLASH = '\\'
DASH = '–'
DOT = '•'


class Just(Enum):
    '''
    Desc:
        Defines three justifications for cells in TableDrawer
    '''
    right = 0
    left = 1
    center = 2


class TableDrawer:
    '''
    Desc:
        This class contains several methods to generate viewable tables from a Table object
    '''

    @staticmethod
    def generateTextTable(table = Table(), col_sep = LINE, row_sep = DASH, justification = Just.right) -> str:
        '''
        Desc:
            Renders a Table object as text

        Parameters:
            table - the Table object to be rendered
            col_sep - the string to be used when separating columns
            row_sep - the string to be used when separating rows
            justification - the justification of the elements in the cell
        '''

        def textifyCell(element, longest_element_length, justification) -> str:
            '''
            Desc:
                Returns a text representation of a cell
            
            Parameters:
                elem - the value to be rendered in the cell
                longest_element_length - length of the longest element in the table
                justification - the justification of the elements in the cell
            '''

            s = ' '
            element = str(element)
            mult = (longest_element_length - len(element))
            if justification is Just.right:
                s += (' ' * mult) + element
            elif justification is Just.left:
                s += element + (' ' * mult)
            elif justification is Just.center:
                if len(element) == longest_elememt_length:
                    s += element
                else:
                    extra = 1 if (longest_elememt_length % 2 != 0) is (len(element) % 2 == 0) else 0
                    s += (' ' * (mult//2 + extra)) + element + (' ' * (mult//2))
            s += ' '
            return s

        # checks if the table is empty
        if len(table.rows) == 0 or len(table.rows[0].cells) == 0:
            return str()
        # creates string
        longest_elememt_length = table.longestElement()
        table_string = str()
        for row in table.rows:
            for cell in row.cells:
                table_string += col_sep + textifyCell(cell.contents, longest_elememt_length, justification)
            table_string += col_sep + '\n'
            if row.is_header:
                table_string += (row_sep * ((longest_elememt_length + 3) * (len(row.cells)) + 1)) + '\n' ## needs tweaking
        return table_string

 

# matrix = [
#     [122314, 3, 1, 623, 31, 8],
#     [142, 1, 124, 7, 9, 1],
#     [0, 16, 0, 122314, 2, 1],
#     [11, 2517, 4, 1, 1, 4]
# ]

# my_table = Table.matrixToTable(matrix, has_header=True)

# print(TableDrawer.generateTextTable(my_table, col_sep=LINE, row_sep=DOT, justification=Just.center))

# print(my_table.asMatrix())