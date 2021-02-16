    def lookup_around(self, queue, x, y):
       
        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            if self.grid[x][y] == '1':
                queue.append((x, y))

    def label_cells(self, row, col):
       
        queue = deque()

        queue.append((row, col))
        while queue:
            x, y = queue.pop()
            self.grid[x][y] = '2'

            self.lookup_around(queue, x - 1, y)
            self.lookup_around(queue, x, y - 1)
            self.lookup_around(queue, x + 1, y)
            self.lookup_around(queue, x, y + 1)
            
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        self.grid = grid

        row_length = len(grid)
        col_length = len(grid[0])

        island_counter = 0
        for y in range(row_length):
            for x in range(col_length):
                if self.grid[y][x] == '1':
                    # found an island
                    island_counter += 1

                    self.label_cells(y, x)

        return island_counter