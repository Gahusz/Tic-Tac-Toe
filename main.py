from functions import who_starts, print_board, choosing_field

starts='X'

win = False


#dictionary
board1 = {'1': ' ', '2': ' ', '3': ' ',
          '4': ' ', '5': ' ', '6': ' ',
          '7': ' ', '8': ' ', '9': ' '}

print_board(board1)

who_starts()

print(starts)
print('-----')
print('1' + '|' + '2' + '|' + '3')
print('-----')
print('4' + '|' + '5' + '|' + '6')
print('-----')
print('7' + '|' + '8' + '|' + '9')
print('-----')
print('choose field please!: ' + str(list(board1.keys())))

choosing_field(starts)