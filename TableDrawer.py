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
        table_string = ''
        for row in table.rows:
            for cell in row.cells:
                table_string += col_sep + ' w '
            table_string += col_sep + '\n'
            if row.is_header:
                table_string += (row_sep * (len(row.cells) * 4 + 1)) + '\n' # this needs to be more expandable
        return table_string



# Testing:

my_table = Table(5, 6)

print(TableDrawer.generateTextTable(my_table))