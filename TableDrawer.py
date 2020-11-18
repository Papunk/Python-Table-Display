from Table import *

# Error 404 documentation not found (yet)

ASTERISK = '*'
HASH = '#'
LINE = '|'
DASH = '–'
DOT = '•'

class TableDrawer:

    @staticmethod
    def generateTextTable(table = Table(), col_sep = LINE, row_sep = DASH) -> str:

        def textifyCell(element, longest_element) -> str: # add justification
            return ' ' + (' ' * (longest_element - len(str(element)))) + str(element) + ' '

        # checks if the table is empty
        if len(table.rows) == 0 or len(table.rows[0].cells) == 0:
            return str()
        # creates string
        longest_elememt = table.longestElement()
        table_string = str()
        for row in table.rows:
            for cell in row.cells:
                table_string += col_sep + textifyCell(cell.contents, longest_elememt)
            table_string += col_sep + '\n'
            if row.is_header:
                table_string += (row_sep * (len(row.cells) * 4 + 1)) + '\n' # this needs to be more expandable
        return table_string

# TODO 
# make the tableDrawer adjust width depending on largest element
# add margin justification

# Testing:

matrix = [
    [211345, 3, 1, 623, 3, 8],
    [1, 1, 4, 7, 9, 1],
    [0, 16, 0, 0, 2, 1],
    [1, 2, 4, 1, 1, 4]
]

my_table = Table.matrixToTable(matrix)

print(TableDrawer.generateTextTable(my_table))