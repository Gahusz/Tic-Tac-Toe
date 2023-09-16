import pprint

import numpy
board1 = {'top-L': 'X', 'top-M': 'X', 'top-R': 'X', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#pprint.pprint(board1)

# def print_board(board):
#     print('-----')
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-----')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-----')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#     print('-----')
#
#
# print_board(board1)
# print('Tic Tac Toe game :) Do you want X or O?Type 1 - X, 2 - O and press enter')
#
#
#
# #while True is infinite loop which can be stopped by for example 'break'
# while True:
#     who_starts = input()
#     if who_starts == '1':
#         starts = 'X'
#         break
#     elif who_starts == '2':
#         starts = 'O'
#         break
#     else:
#         print('Write \'1\' or \'2\' please!')
#         print('Do you want X or O? 1 - X, 2 - O and enter')
#
#
#
# print(who_starts)
# print('-----')
# print('1' + '|' + '2' + '|' + '3')
# print('-----')
# print('4' + '|' + '5' + '|' + '6')
# print('-----')
# print('7' + '|' + '8' + '|' + '9')
# print('-----')
# print('choose field please!: 1,2,3,4,5,6,7,8 or 9')
# field=input()
pip --version
#values = board1.values()

#horizontal
for i in values.arange(0, len(values), 3):
    if values[i:i+2] == 'X':
        print('X wins!')
    if values[i:i+2] == 'O':
        print('O wins!')
# if i
# vertical
# if


# keys=list(board1.keys())
# keys[1]
# for i in keys:
#     print(i)




#print('\n'+ board1['top-L'])

