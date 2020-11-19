from Table import *
from enum import Enum

# Error 404 documentation not found (yet)

ASTERISK = '*'
HASH = '#'
LINE = '|'
DASH = '–'
DOT = '•'


class Just(Enum):
        right = 0
        left = 1
        center = 2


class TableDrawer:

    @staticmethod
    def generateTextTable(table = Table(), col_sep = LINE, row_sep = DASH, justification = Just.right) -> str:

        def textifyCell(element, longest_element, justification) -> str: # add justification
            s = ' '
            if justification is Just.right:
                s += (' ' * (longest_element - len(str(element)))) + str(element)
            elif justification is Just.left:
                s += str(element) + (' ' * (longest_element - len(str(element))))
            elif justification is Just.center:
                s += (' ' * ((longest_element - len(str(element)))//2 + (1 if len(str(element)) % 2 == 0 else 0 ))) +str(element) + (' '  * ((longest_element - len(str(element)))//2))
            s += ' '
            return s

        # checks if the table is empty
        if len(table.rows) == 0 or len(table.rows[0].cells) == 0:
            return str()
        # creates string
        longest_elememt = table.longestElement()
        table_string = str()
        for row in table.rows:
            for cell in row.cells:
                table_string += col_sep + textifyCell(cell.contents, longest_elememt, justification)
            table_string += col_sep + '\n'
            if row.is_header:
                table_string += (row_sep * ((longest_elememt + 3) * (len(row.cells)) + 1)) + '\n'
        return table_string

# TODO 
# fix bug where if longest element is even, center justified tables get messed up

# Testing:

matrix = [
    [176473, 3, 1, 623, 31, 8],
    [142, 1, 4, 7, 9, 1],
    [0, 16, 0, 0, 2, 1],
    [11, 2567, 4, 1, 1, 4]
]

my_table = Table.matrixToTable(matrix, has_header=True)

print(TableDrawer.generateTextTable(my_table, justification=Just.center))