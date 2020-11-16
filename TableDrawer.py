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
        # checks if the table is empty
        if len(table.rows) == 0 or len(table.rows[0].cells) == 0:
            return str()
        # creates string
        table_string = str()
        for row in table.rows:
            for cell in row.cells:
                table_string += col_sep + ' ' + str(cell.contents) + ' '
            table_string += col_sep + '\n'
            if row.is_header:
                table_string += (row_sep * (len(row.cells) * 4 + 1)) + '\n' # this needs to be more expandable
        return table_string



# Testing:

matrix = [
    [2, 3, 1, 6, 3, 8],
    [1, 1, 4, 7, 9, 1],
    [0, 6, 0, 0, 2, 1],
    [1, 2, 4, 1, 1, 4]
]

my_table = Table.matrixToTable()


print(TableDrawer.generateTextTable(my_table))