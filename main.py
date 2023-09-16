

import plansza
from plansza import print_board
from plansza import check_win
#import numpy
global win

board1 = {'1': ' ', '2': ' ', '3': ' ',
          '4': ' ', '5': ' ', '6': ' ',
          '7': ' ', '8': ' ', '9': ' '}

#pprint.pprint(board1)
#print_board(board1)


print('Tic Tac Toe game :) Do you want X or O? Type 1 - X, 2 - O and press enter')



#while True is infinite loop which can be stopped by for example 'break'
while True:
    who_starts = input()
    if who_starts == '1':
        starts = 'X'
        break
    elif who_starts == '2':
        starts = 'O'
        break
    else:
        print('Write \'1\' or \'2\' please!')
        print('Do you want X or O? 1 - X, 2 - O and enter')



print(who_starts)
print('-----')
print('1' + '|' + '2' + '|' + '3')
print('-----')
print('4' + '|' + '5' + '|' + '6')
print('-----')
print('7' + '|' + '8' + '|' + '9')
print('-----')
print('choose field please!: 1,2,3,4,5,6,7,8 or 9')

while True:
    if starts== 'X':
        field = input()
        values = list(board1.values())
        if field in board1:
            if board1[field]==' ':
                board1[field]='X'
                check_win()
                if win==True:
                    break
                else:
                    starts='O'
            else:
                print('This field is taken. Choose other field')
        else:
            print('Wrong field.' + 'Choose field from: ' + list(board1.keys()))

    elif starts == 'O':
        field = input()
        values = list(board1.values())
        if field in board1:
            if board1[field] == ' ':
                board1[field] = 'O'
                check_win()
                if win==True:
                    break
                else:
                    starts='X'
        else:
            print('This field is taken. Choose other field')
    else:
        print('Wrong field.' + 'Choose field from: ' + list(board1.keys()))


#indent - akapit

check_win()





