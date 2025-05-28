import random

class Minesweeper:
    def __init__(self, size=9, mines=10):
        self.size = size  # Размер поля (например, 9x9)
        self.mines = mines  # Количество мин
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.revealed = [[False for _ in range(size)] for _ in range(size)]
        self.game_over = False
        self.initialize_board()

    def initialize_board(self):
        # Размещение мин случайным образом
        mines_placed = 0
        while mines_placed < self.mines:
            x = random.randint(0, self.size -1)
            y = random.randint(0, self.size -1)
            if self.board[x][y] != 'M':
                self.board[x][y] = 'M'
                mines_placed +=1
        # Заполнение чисел
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] != 'M':
                    self.board[x][y] = self.count_mines(x, y)

    def count_mines(self, x, y):
        count =0
        for i in range(max(0, x-1), min(self.size, x+2)):
            for j in range(max(0, y-1), min(self.size, y+2)):
                if self.board[i][j] == 'M':
                    count +=1
        return str(count)

    def reveal_cell(self, x, y):
        if x <0 or x >= self.size or y <0 or y >= self.size:
            print("Некорректные координаты!")
            return
        if self.revealed[x][y]:
            print("Клетка уже открыта.")
            return
        self.revealed[x][y] = True
        if self.board[x][y] == 'M':
            self.game_over = True
            print("Вы наткнулись на мину! Игра окончена.")
            self.print_board(reveal=True)
            return
        if self.board[x][y] == '0':
            # Рекурсивное открытие соседних клеток
            for i in range(max(0, x-1), min(self.size, x+2)):
                for j in range(max(0, y-1), min(self.size, y+2)):
                    if not self.revealed[i][j]:
                        self.reveal_cell(i, j)

if __name__ == "__main__":
    size = 9
    mines = 10
    game = Minesweeper(size, mines)
    game.play()
