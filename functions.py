import sys
import numpy

again = ' '

starts='X'

#dictionary
board1 = {'1': ' ', '2': ' ', '3': ' ',
          '4': ' ', '5': ' ', '6': ' ',
          '7': ' ', '8': ' ', '9': ' '}
#############################################################


def print_board(board):

    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
#############################################################

#############################################################
def who_starts():
    global starts
    print('Tic Tac Toe game :) Do you want X or O? Type \'1\' for X, \'2\' for O and press enter')

# if I name inside function variable with the same name as global variable I will shadow it (przesłonięcie)

#while True is infinite loop which can be stopped by for example 'break'
    while True:
        starts = input()
        if starts == '1':
            return 'X'
        elif starts == '2':
            return 'O'
        else:
            print('Write \'1\' or \'2\' please!')
            print('Do you want X or O? 1 - X, 2 - O and enter')

####################################################################

def restart():
    global board1
    global again

    while True:
        print('Do you want to play again? 1 - yes 2 - no')
        again = input()
        if again == "1":
            break
        elif again == "2":
            print('Goodbye')
            sys.exit(0)
        else:
            print('Please enter \'1\' or \'2\'.')
#############################################################


#############################################################
def choosing_field(starting):
    global board1
    #nested functions
    def check_win(board):
        global board1
        values = list(board.values())

        # horizontal

        # THIS IS WRONG beacuse I can't compare to single character to get good result
        # for i in numpy.arange(0, len(values), 3):
        #     if values[i:i+2] == 'X':
        #         print('X wins!')
        #     if values[i:i+2] == 'O':
        #         print('O wins!')
        # I have to use list comprehension
        for i in numpy.arange(0, len(values), 3):
            if all(x == 'X' for x in values[i:i + 3]):
                print('X wins!')
                board1 = {'1': ' ', '2': ' ', '3': ' ',
                          '4': ' ', '5': ' ', '6': ' ',
                          '7': ' ', '8': ' ', '9': ' '}
                restart()
            if all(o == 'O' for o in values[i:i + 3]):
                print('O wins!')
                board1 = {'1': ' ', '2': ' ', '3': ' ',
                          '4': ' ', '5': ' ', '6': ' ',
                          '7': ' ', '8': ' ', '9': ' '}
                restart()

        # vertical

        for i in numpy.arange(0, 3):
            if all(x == 'X' for x in values[i::3]):  # start:stop:step i::3 is start from i end empty step 3
                print('X wins!')
                board1 = {'1': ' ', '2': ' ', '3': ' ',
                          '4': ' ', '5': ' ', '6': ' ',
                          '7': ' ', '8': ' ', '9': ' '}
                restart()
            if all(o == 'O' for o in values[i::3]):
                print('O wins!')
                board1 = {'1': ' ', '2': ' ', '3': ' ',
                          '4': ' ', '5': ' ', '6': ' ',
                          '7': ' ', '8': ' ', '9': ' '}
                restart()

        # diagonally
        diagonal1 = [0, 4, 8]
        diagonal2 = [2, 4, 6]

        if all(values[x] == 'X' for x in diagonal1):  # if I dont write =='X' it will check if field is empty only
            print('X wins!')
            board1 = {'1': ' ', '2': ' ', '3': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '7': ' ', '8': ' ', '9': ' '}
            restart()
        if all(values[o] == 'O' for o in diagonal1):
            print('O wins!')
            board1 = {'1': ' ', '2': ' ', '3': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '7': ' ', '8': ' ', '9': ' '}
            restart()
        if all(values[x] == 'X' for x in diagonal2):
            print('X wins!')
            board1 = {'1': ' ', '2': ' ', '3': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '7': ' ', '8': ' ', '9': ' '}
            restart()
        if all(values[o] == 'O' for o in diagonal2):
            print('O wins!')
            board1 = {'1': ' ', '2': ' ', '3': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '7': ' ', '8': ' ', '9': ' '}
            restart()

            #draw
        if ' ' not in values:
            print('Draw!')
            board1 = {'1': ' ', '2': ' ', '3': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '7': ' ', '8': ' ', '9': ' '}
            restart()


#########################################################
    while True:
        if starting == 'X':
            field = input()
            if field in board1:
                if board1[field] == ' ':
                    board1[field] = 'X'
                    print_board(board1)
                    check_win(board1)
                    starting = 'O'
                    if again == "1":
                        break
                else:
                    print('This field is taken. Choose other field')

            else:
                print('Wrong field.' + 'Choose field from: ' + str(list(board1.keys())))

        else:
            starting = 'O'
            field = input()
            if field in board1:
                if board1[field] == ' ':
                    board1[field] = 'O'
                    print_board(board1)
                    check_win(board1)
                    starting = 'X'
                    if again == "1":
                        break
                else:
                    print('This field is taken. Choose other field')
            else:
                print('Wrong field.' + 'Choose field from: ' + str(list(board1.keys())))




#############################################################