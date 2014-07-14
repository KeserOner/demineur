class Grille:

    def __init__(self, rows, column):
        self.rows = rows
        self.column = column
        self.grid = []
        line = []
        i = 0
        j = 0
        while (i < rows):
            j = 0
            while (j < column):
                line.append('*   ')
                j += 1
            self.grid.append(line)
            i += 1

    def __str__(self):
        for line in self.grid:
            print '{} \n'.format(line)

    def fillGrid(self, mode):
        places = self.rows * self.column
        i = 0
        if (mode == 'hard'):
            mines = places * 0.75
