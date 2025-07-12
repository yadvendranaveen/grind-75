class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0]*26 for _ in range(rows)]
        
    def _get_grid_mapping(self, cell):
        col, row = cell[0], cell[1:]
        # return (ord(col)-65, int(row)-1)
        return (int(row)-1, ord(col)-65)

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._get_grid_mapping(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        ans = 0
        for x in formula[1:].split('+'):
            if x.isnumeric():
               ans += int(x) 
            else:
                row, col = self._get_grid_mapping(x)
                ans += self.grid[row][col]
        return ans


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)