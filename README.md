# Python-Table-Display
This program models, displays, and formats tables in configurable ways.

For example, the following code

```
matrix = [
    [122314, 3, 1, 623, 31, 8],
    [142, 1, 124, 7, 9, 1],
    [0, 16, 0, 122314, 2, 1],
    [11, 2517, 4, 1, 1, 4]
]

my_table = Table.matrixToTable(matrix, has_header=True)

print(TableDrawer.generateTextTable(my_table, col_sep=LINE, row_sep=DOT, justification=Just.center))
```

generates the follorwing string:

```
| 122314 |    3   |    1   |   623  |   31   |    8   |
•••••••••••••••••••••••••••••••••••••••••••••••••••••••
|   142  |    1   |   124  |    7   |    9   |    1   |
|    0   |   16   |    0   | 122314 |    2   |    1   |
|   11   |  2517  |    4   |    1   |    1   |    4   |
```
