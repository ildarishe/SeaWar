class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


class Ship:
    def __init__(self, len, p, dir):
        self.p = p
        self.len = len
        self.dir = dir
        self.lifes = len

    def dots(self):
        points = [self.p]
        curx = self.p.x
        cury = self.p.y
        for i in range(self.len):
            if self.dir:
                curx += 1
            else:
                cury += 1
            points.append(Dot(curx, cury))
        return points

    def hit(self, shot):
        return shot in self.dots()



class Board:
    def __init__(self, ships, size=6):
        self.size = size
        self.field = [[0 for i in range(size)] for j in range(size)]
        print(self.field)
    def print_board(self):
        print(" | "  + " | ".join([str(i + 1) for i in range(self.size)]) + " |")
        for i in range(self.size):
            print(chr(ord("A") + i), end=" ")
            for j in range(self.size):
                print(self.field[i][j], end=" ")
            print()


class Player:
    def __init__(self, my_board, other_board):
        self.my = my_board
        self.enemy = other_board

    def ask(self):
        pass

    def move(self):
        pass

class Ai(Player):
    pass

class User(Player):
    pass
a = Dot(1, 2)
s = Ship(4, a, 1)
x = Dot(6, 2)
print(s.hit(x))
b = Board(a)
b.print_board()