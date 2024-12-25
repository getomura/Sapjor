import random

class Minesweeper:

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

    def play(self):
        while not self.game_over:
            self.print_board()
            try:
                user_input = input("Введите координаты для открытия (строка столбец) или 'q' для выхода: ")
                if user_input.lower() == 'q':
                    print("Игра завершена пользователем.")
                    break
                x, y = map(int, user_input.strip().split())
                self.reveal_cell(x, y)
                if self.check_win():
                    print("Поздравляем! Вы выиграли!")
                    self.print_board(reveal=True)
                    break
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите два числа, разделённых пробелом.")

if __name__ == "__main__":
    size = 9
    mines = 10
    game = Minesweeper(size, mines)
    game.play()
