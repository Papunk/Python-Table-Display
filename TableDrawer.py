# documentation not found (yet)

ASTERISK = '*'
HASH = '#'
LINE = '|'
DASH = '–'
DOT = '•'

class TableDrawer:

    @staticmethod
    def generateTextTable(table = Table(), separator = '|') -> str:
        for row in table.table: