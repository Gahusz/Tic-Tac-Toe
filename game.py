import sys
import numpy


class Game:

    def __init__(self):
        self._again = " "
        self.X_score = 0
        self.O_score = 0
        self.board = {
            "1": " ",
            "2": " ",
            "3": " ",
            "4": " ",
            "5": " ",
            "6": " ",
            "7": " ",
            "8": " ",
            "9": " ",
        }
        # this has to be after after board is initialized because ask_who_starts uses board
        self.who_starts = self.ask_who_starts()

    # printing board
    def __str__(self):
        return (
            "-----\n"
            "1|2|3\n"
            "-----\n"
            "4|5|6\n"
            "-----\n"
            "7|8|9\n"
            "-----\n"
            "\n"
            "-----\n"
            f"{self.board['1']}|{self.board['2']}|{self.board['3']}\n"
            "-----\n"
            f"{self.board['4']}|{self.board['5']}|{self.board['6']}\n"
            "-----\n"
            f"{self.board['7']}|{self.board['8']}|{self.board['9']}\n"
            "-----\n"
            "Choose field please!: " + str(list(self.board.keys()))
        )

    def print_board(self):
        print(self)

    def ask_who_starts(self):
        while True:
            self.who_starts = input(
                "Who starts? Type '1' for X, '2' for O and press enter: "
            )
            if self.who_starts == "1":
                print("X starts!")
                self.print_board()
                return "X"
            elif self.who_starts == "2":
                print("O starts!")
                self.print_board()
                return "O"
            else:
                print("Write '1' or '2' please! ")

    def choosing_field(self):
        while True:
            if self.who_starts == "X":
                field = input()
                if field in self.board:
                    if self.board[field] == " ":
                        self.board[field] = "X"
                        self.print_board()
                        self.check_win()
                        self.who_starts = "O"
                    else:
                        print("This field is taken. Choose other field.  ")

                else:
                    print(
                        "Wrong field."
                        + "Choose field from: "
                        + str(list(self.board.keys()))
                    )

            else:
                self.who_starts = "O"
                field = input()
                if field in self.board:
                    if self.board[field] == " ":
                        self.board[field] = "O"
                        self.print_board()
                        self.check_win()
                        self.who_starts = "X"
                    else:
                        print("This field is taken. Choose other field. ")
                else:
                    print(
                        "Wrong field."
                        + "Choose field from: "
                        + str(list(self.board.keys()))
                    )

    def check_win(self):
        values = list(self.board.values())
        for character in ["X", "O"]:
            # horizontal check
            for i in numpy.arange(0, len(values), 3):
                if all(x == character for x in values[i : i + 3]):
                    print(f"{character} wins!")
                    if character == "X":
                        self.X_score += 1
                    else:
                        self.O_score += 1
                    self.display_points()
                    self.restart_game()
                    return

            # vertical check
            for i in numpy.arange(0, 3):
                if all(x == character for x in values[i::3]):
                    print(f"{character} wins!")
                    if character == "X":
                        self.X_score += 1
                    else:
                        self.O_score += 1
                    self.display_points()
                    self.restart_game()
                    return

            # diagonal check
            diagonals = [[0, 4, 8], [2, 4, 6]]  # Diagonal indices
            for diagonal in diagonals:
                if all(values[x] == character for x in diagonal):
                    print(f"{character} wins!")
                    if character == "X":
                        self.X_score += 1
                    else:
                        self.O_score += 1
                    self.display_points()
                    self.restart_game()
                    return

        # check for draw
        if " " not in values:
            print("Draw! Each player receives 0.5 points.")
            self.O_score += 0.5
            self.X_score += 0.5
            self.display_points()
            self.restart_game()

    def display_points(self):
        print(f"The score for X is: {self.X_score}")
        print(f"The score for O is: {self.O_score}")

    def restart_points(self):
        self.X_score = 0
        self.O_score = 0

    def restart_game(self):
        while True:
            self._again = input('Do you want to play again? "1" - yes; "2" - no. \n')
            if self._again == "1":
                while True:
                    do_you_restart = input(
                        'Do you want to restart points? Write "yes" or "no". \n'
                    )
                    if do_you_restart == "yes":
                        self.board = {
                            "1": " ",
                            "2": " ",
                            "3": " ",
                            "4": " ",
                            "5": " ",
                            "6": " ",
                            "7": " ",
                            "8": " ",
                            "9": " ",
                        }
                        self.restart_points()
                        self.print_board()
                        self.who_starts()
                        self.choosing_field()
                        # return
                    elif do_you_restart == "no":
                        self.board = {
                            "1": " ",
                            "2": " ",
                            "3": " ",
                            "4": " ",
                            "5": " ",
                            "6": " ",
                            "7": " ",
                            "8": " ",
                            "9": " ",
                        }
                        self.print_board()
                        self.ask_who_starts()
                        self.choosing_field()
                        # return  # Break out of all loops after choosing fields
                    else:
                        print('Please enter "yes" or "no".')
            elif self._again == "2":
                print(
                    f"X scored {self.X_score} points and O player scored {self.O_score} points."
                )
                print("Goodbye")
                sys.exit(0)
            else:
                print("Please enter '1' or '2'.")
