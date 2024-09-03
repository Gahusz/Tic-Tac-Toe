from functions import who_starts, print_board, choosing_field
from functions import board1
import argparse

def main():
    while True:
        print_board(board1)

        starts = who_starts()

        print(starts)
        print("-----")
        print("1" + "|" + "2" + "|" + "3")
        print("-----")
        print("4" + "|" + "5" + "|" + "6")
        print("-----")
        print("7" + "|" + "8" + "|" + "9")
        print("-----")
        print("choose field please!: " + str(list(board1.keys())))
        choosing_field(starts)


if __name__ == "__main__":
    main()
