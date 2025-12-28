# grid = [[1,2,3], [4,5,6], [7,8,9]]


# for i in range(0, len(grid)):
#     for j in range(0, len(grid[i])):
#         print(grid[i][j])


# rows = 3
# cols = 3
# total_cells = rows * cols
# grid = []

# i = 0
# while i < total_cells:
#     for r in range(0, rows):
#         temp_row = []
#         for c in range(0, cols):
#             temp_row.append(i+1)
#             i += 1
#         grid.append(temp_row)

# print(grid)

# for i in range(0, total_cells):
#     for j in range(0, rows):
#         print(i)

from collections import namedtuple
Coords = namedtuple('Coords', ['row', 'col'])


class GridPoint:
    def __init__(self, grid, coords):
        self.grid = grid
        self.row = coords.row
        self.col = coords.col
        self.adj_papers = 0

        self.get_adjacents()
        self.count_adj_papers()


    def get_adjacents(self):
        self.adj_n = Coords(row=self.row-1, col=self.col)
        self.adj_nw = Coords(row=self.row-1, col=self.col-1)
        self.adj_ne = Coords(row=self.row-1, col=self.col+1)

        self.adj_s = Coords(row=self.row+1, col=self.col)
        self.adj_sw = Coords(row=self.row+1, col=self.col-1)
        self.adj_se = Coords(row=self.row+1, col=self.col+1)

        self.adj_w = Coords(row=self.row, col=self.col-1)
        self.adj_e = Coords(row=self.row, col=self.col+1)

    def count_adj_papers(self):
        try:
            if self.grid[self.adj_n.row][self.adj_n.col] == '@' and (self.adj_n.row >= 0 and self.adj_n.col >= 0):
                # print(self.adj_n)
                self.adj_papers += 1
        except IndexError as e:
            pass

        try:
            if self.grid[self.adj_nw.row][self.adj_nw.col] == '@' and (self.adj_nw.row >= 0 and self.adj_nw.col >= 0):
                # print(self.adj_nw)
                self.adj_papers += 1
        except IndexError as e:
            pass

        try:
            if self.grid[self.adj_ne.row][self.adj_ne.col] == '@' and (self.adj_ne.row >= 0 and self.adj_ne.col >= 0):
                # print(self.adj_ne)
                self.adj_papers += 1
        except IndexError as e:
            pass

        try:
            if self.grid[self.adj_s.row][self.adj_s.col] == '@' and (self.adj_s.row >= 0 and self.adj_s.col >= 0):
                # print(self.adj_s)
                self.adj_papers += 1
        except IndexError as e:
            pass

        try:
            if self.grid[self.adj_sw.row][self.adj_sw.col] == '@' and (self.adj_sw.row >= 0 and self.adj_sw.col >= 0):
                # print(self.adj_sw)
                self.adj_papers += 1
        except IndexError as e:
            pass

        try:
            if self.grid[self.adj_se.row][self.adj_se.col] == '@' and (self.adj_se.row >= 0 and self.adj_se.col >= 0): 
                # print(self.adj_se)
                self.adj_papers += 1
        except IndexError as e:
            pass

        try:
            if self.grid[self.adj_w.row][self.adj_w.col] == '@' and (self.adj_w.row >= 0 and self.adj_w.col >= 0):
                # print(self.adj_w)
                self.adj_papers += 1
        except IndexError as e:
            pass

        try:
            if self.grid[self.adj_e.row][self.adj_e.col] == '@' and (self.adj_e.row >= 0 and self.adj_e.col >= 0):
                # print(self.adj_e)
                self.adj_papers += 1
        except IndexError as e:
            pass
        

def pretty_print_grid(grid):
    for i in grid:
        print(i)


if __name__ == '__main__':
    grid = []
    total_removed = 0

    with open('input.txt', 'r') as f:
        for line in f:
            row = []
            for hole in line.strip('\n'):
                row.append(hole)
            grid.append(row)

    # pretty_print_grid(grid)
    while True:
        papers = []
        for i, shelf in enumerate(grid):
            # print(f"Processing: {shelf}")
            for j, hole in enumerate(shelf):
                # print(f"Processing: {hole}")
                if hole == '@':
                    paper = GridPoint(grid, Coords(row=i, col=j))
                    # print(f"Paper found. {paper.row},{paper.col}...{paper.adj_papers}")
                    if paper.adj_papers < 4:
                        papers.append(paper)
        if len(papers):

            # print(len(papers))
            total_removed += len(papers)

            for p in papers:
                grid[p.row][p.col] = "."
        else:
            break

    print(total_removed)


        
    
   