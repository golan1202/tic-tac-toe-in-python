
class XOBoard:
    def __init__(self):
        self.move_number = 0
        self.M = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]
        self.USER_X = "X"
        self.USER_O = "O"
        self.state = ["X wins", "O wins", "Draw", "Game not finished"]

    def display(self):
        print("\n   1  2  3")
        print("  ---------")
        i = 0
        for row in self.M:
            i += 1
            print(f"{i} |", end=' ')
            for elem in row:
                print(elem, end=' ')
            print("|")
        print("  ---------\n")

    def count_empty_cells(self):
        empty_cells = 0
        for row in self.M:
            for elem in row:
                if elem == " ":
                    empty_cells += 1
        return empty_cells

    def win(self, user):
        # cases 1,2,3 - row solutions
        case1 = self.M[0][0] == self.M[0][1] == self.M[0][2] == user
        case2 = self.M[1][0] == self.M[1][1] == self.M[1][2] == user
        case3 = self.M[2][0] == self.M[2][1] == self.M[2][2] == user
        # cases 4,5,6 - columns solutions
        case4 = self.M[0][0] == self.M[1][0] == self.M[2][0] == user
        case5 = self.M[0][1] == self.M[1][1] == self.M[2][1] == user
        case6 = self.M[0][2] == self.M[1][2] == self.M[2][2] == user
        # diagonal solutions
        case7 = self.M[0][0] == self.M[1][1] == self.M[2][2] == user
        case8 = self.M[2][0] == self.M[1][1] == self.M[0][2] == user
        if case1 or case2 or case3 or case4 or case5 or case6 or case7 or case8:
            return True

    def status(self):
        if self.win(self.USER_X):
            return self.state[0]
        elif self.win(self.USER_O):
            return self.state[1]
        elif self.count_empty_cells() == 0:
            return self.state[2]
        else:
            return self.state[3]

    def put(self, cor1, cor2):
        cor1 -= 1
        cor2 -= 1
        if self.M[cor1][cor2] != self.USER_X and self.M[cor1][cor2] != self.USER_O:
            if self.player_turn() == self.USER_X:
                self.M[cor1][cor2] = self.USER_X
            else:
                self.M[cor1][cor2] = self.USER_O
        else:
            print("This cell is occupied! Choose another one!")
            return False
        self.move_number += 1
        return True

    def player_turn(self):
        if self.move_number % 2 == 0:
            return self.USER_X
        return self.USER_O

    def display_and_status(self):
        self.display()
        print(self.status())

    def run(self):
        self.display()
        while True:
            print(f'Player "{self.player_turn()}" turn.\nEnter the coordinates:')
            try:
                (cor1, cor2) = [int(x) for x in input().split(' ')]
                if self.put(cor1, cor2):
                    if self.status() == self.state[0] or self.status() == self.state[1] or self.status() == self.state[2]:
                        self.display_and_status()
                        return True
                    else:
                        self.display_and_status()

            except (ValueError, TypeError):
                print("You should enter only 2 numbers!")
            except (OverflowError, IndexError):
                print("Coordinates should be from 1 to 3!")


