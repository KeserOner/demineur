import random


class Grille:

    def __init__(self, rows, column):
        self.rows = rows
        self.column = column
        self.grid = []
        self.game = []

        for i in range(rows):
            line = []
            game_line = []

            for j in range(column):
                line.append(False)
                game_line.append('*   ')

            self.grid.append(line)
            self.game.append(game_line)

    def __repr__(self):
        return "%d %d" % (self.rows, self.column)

    def displayGrid(self):
        for line in self.grid:
            string = ''
            for elt in line:
                if not elt:
                    string += '*   '
                else:
                    string += 'x   '
            print "%r \n" % (string)

    def displayGame(self):
        for line in self.game:
            print '%r \n' % (''.join(line))
        print '\n\n\n'

    def fillGrid(self, mode):
        places = self.rows * self.column

        if (mode == 'hard'):
            mines = int(places * 0.75)
        elif (mode == 'medium'):
            mines = int(places * 0.5)
        else:
            mines = int(places * 0.25)

        for i in range(mines):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.column - 1)
            self.grid[x][y] = True

    def getNeighboor(self, x, y):
        min_col = y - 1
        max_col = y + 1
        min_row = x - 1
        max_row = x + 1
        l = []
        if x == 0:
            min_row = 0
        elif x == self.rows - 1:
            max_row = self.rows - 1

        if y == 0:
            min_col = 0
        elif y == self.column - 1:
            max_col = self.column - 1

        i = min_row
        while i <= max_row:
            j = min_col
            while j <= max_col:
                l.append((i, j))
                j += 1
            i += 1
        return l

    def checkNeighboor(self, x, y):
        count = 0
        liste = self.getNeighboor(x, y)
        for point in liste:
            if self.grid[point[0]][point[1]]:
                count += 1
        return count

    def partyOver(self):
        for line in self.game:
            if '*   ' in line:
                return False
        return True

    def playAShot(self, x, y, flag, checked):
        if flag:
            self.game[x][y] = 'f   '
        else:
            checked[x][y] = True
            shot = self.checkNeighboor(x, y)
            self.game[x][y] = '%s   ' % (str(shot))
            if shot == 0:
                li = self.getNeighboor(x, y)
                for point in li:
                    if not checked[point[0]][point[1]]:
                        self.playAShot(point[0], point[1], False, checked)

    def playAGame(self):
        flag = False
        choice_flag = raw_input('Flag ?: Y/N  ')
        choice_x = input('Enter a row: ')
        x = int(choice_x)
        choice_y = input('Enter a column: ')
        y = int(choice_y)
        if choice_flag == 'Y' or choice_flag == 'y':
            flag = True
        if not flag and self.grid[x][y]:
            self.game[x][y] = 'x  '
            self.displayGame()
            return False
        checked = []
        for line in self.game:
            check = []
            for el in line:
                check.append(False)
            checked.append(check)
        self.playAShot(x, y, flag, checked)
        self.displayGame()
        return True


    def playAParty(self):
        pag = self.playAGame()
        po = self.partyOver()
        while pag and not po:
            pag = self.playAGame()
            po = self.partyOver()

        if self.partyOver():
            print 'Congratulation, you win !'
        else:
            print 'Game Over Bitch !'
