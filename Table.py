class Cell:

    def __init__(self, contents):
        self.contents = contents


class Row:

    def __init__(self, length = 0):
        self.length = length
    

class Table:

    def __init__(self, numOfRows = 0, cellsPerRow = 0):
        self.table = []
	for _ in range(numOfRows):
		self.table.append(Row(cellsPerRow))


