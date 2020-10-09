# Earlier in the course, you implemented a function that could
# find if someone had won a particular game of either tic-tac-
# toe or mancala based on a 2D list or tuple representing the
# current game board.
#
# In this problem, you'll do the same thing, but for the game
# Connect 4. Write a function called check_winner which takes
# as input a 2D list. It should return "X" if there are four
# adjacent "X" values anywhere in the list (row, column,
# diagonal); "O" if there are four adjacent "O" values
# anywhere in the list; and None if there are neither.
#
# Here are the ways Connect-4 is different from tic-tac-toe:
#
# - Connect-4 is played with 6 rows and 7 columns, not 3
#   rows and 3 columns.
# - You must have 4 in a row (or column or diagonal) to win
#   instead of 3.
# - You may only place pieces in the bottom-most empty
#   space in a column (e.g. you "drop" the pieces in the
#   column and they fall to the first empty spot). Note,
#   though, that this shouldn't affect your reasoning.
#
# To keep things simple, we'll still use "X" and "O" to
# represent the players, and None to represent empty spots.
# You may assume there will be only one winner per board,
# no characters besides "X", "O", and None, and you don't
# have to worry about whether the board is actually a
# valid game of Connect 4.
#
# Hints:
# - Don't forget both kinds of diagonals, top-left to
#   bottom-right and bottom-left to top-right.
# - This board is too large to check every possible place
#   for a winner: there are 69 places a player could win.
# - Remember, if you put a negative index in a list,
#   Python "wraps around" and checks the last value. You
#   may have to control for this.


# Write your function here!

def check_winner(board):
    ROWS_COUNT = 6
    COLUMNS_COUNT = 7

    # check for horizontal winning
    for col in range(COLUMNS_COUNT - 3):
        for row in range(ROWS_COUNT):
            if board[row][col]:
                current_player = board[row][col]
                if current_player == board[row][col + 1] and current_player == board[row][col + 2]\
                    and current_player == board[row][col + 3]:
                    return current_player, 'Horizantol winning'
            else:
                continue
    # check for vertical winning
    for col in range(COLUMNS_COUNT):
        for row in range(ROWS_COUNT - 3):
            if board[row][col]:
                current_player = board[row][col]
                if current_player == board[row + 1][col] and current_player == board[row + 2][col]\
                    and current_player == board[row + 3][col]:
                    return current_player, 'Vertical winning'
            else:
                continue

    # check for bottom-left to top-right diagonal
    for col in range(COLUMNS_COUNT - 3):
        for row in range(ROWS_COUNT - 3):
            if board[row][col]:
                current_player = board[row][col]
                if current_player == board[row + 1][col + 1] and current_player == board[row + 2][col + 2]\
                    and current_player == board[row + 3][col + 3]:
                    return current_player, 'top-left to bottom-right diagnal winning'
            else:
                continue

    # check for top-left to bottom-right diagonal
    for col in range(COLUMNS_COUNT - 3):
        for row in range(3, ROWS_COUNT):
            if board[row][col]:
                current_player = board[row][col]
                if current_player == board[row - 1][col + 1] and current_player == board[row - 2][col + 2]\
                    and current_player == board[row - 3][col + 3]:
                    return current_player, 'bottom-left to top-right diagnal winning'
            else:
                continue
    return 'No Winner'


# The code below tests your function on three Connect-4
# boards. Remember, the line breaks are not needed to create
# a 2D tuple; they're used here just for readability.
xwins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         (None, None, None, None, "X" , None, None),
         (None, None, None, "X" , "O" , "O" , None),
         (None, "O" , "X" , "X" , "O" , "X" , None),
         ("O" , "X"  ,"O" , "O" , "O" , "X" , "X"))

owins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         ("O" , "O" , "O" , "O" , None, None, None),
         ("O" , "X" , "X" , "X" , None, None, None),
         ("X" , "X" , "X" , "O" , "X" , None, None),
         ("X" , "O" , "O" , "X" , "O" , None, None))

nowins = (("X" , "X" , None, None, None, None, None),
          ("O" , "O" , None, None, None, None, None),
          ("O" , "X" , "O" , "O" , None, "O" , "O" ),
          ("O" , "X" , "X" , "X" , None, "X" , "X" ),
          ("X" , "X" , "X" , "O" , "X" , "X" , "O" ),
          ("X" , "O" , "O" , "X" , "O" , "X" , "O" ))

game_board = (('X', 'X', 'O', 'X', 'X', 'X', 'O'),
              ('O', 'O', 'X', 'O', 'O', 'X', 'O'),
              ('O', 'X', 'O', 'O', 'X', 'O', 'O'),
              ('O', 'X', 'X', 'X', 'O', 'X', 'X'),
              ('X', 'X', 'X', 'O', 'X', 'X', 'O'),
              ('X', 'O', 'O', 'X', 'O', 'X', 'O'))


h_o = (('X', 'X', 'O', 'O', 'X', 'X', 'X'),
        ('O', 'O', 'X', 'O', 'O', 'X', 'O'),
        ('O', 'X', 'O', 'O', 'X', 'O', 'O'),
        ('O', 'X', 'X', 'X', 'O', 'X', 'X'),
        ('X', 'X', 'X', 'O', 'X', 'X', 'O'),
        ('X', 'O', 'O', 'O', 'O', 'X', 'O'))

v_x = (('X', 'X', 'O', 'X', 'X', 'X', 'O'),
        ('X', 'O', 'X', 'O', 'O', 'X', 'O'),
        ('X', 'X', 'O', 'O', 'X', 'O', 'O'),
        ('X', 'X', 'X', 'O', 'O', 'X', 'X'),
        ('O', 'X', 'X', 'O', 'X', 'X', 'O'),
        ('O', 'O', 'O', 'X', 'O', 'X', 'O'))

d_x1 =  (
        ('X', 'X', 'O', 'X', 'X', 'O', 'O'),
        ('O', 'O', 'X', 'O', 'O', 'X', 'O'),
        ('O', 'X', 'O', 'X', 'X', 'O', 'O'),
        ('O', 'X', 'X', 'X', 'O', 'X', 'X'),
        ('X', 'X', 'X', 'O', 'X', 'X', 'O'),
        ('X', 'O', 'O', 'X', 'O', 'X', 'O'))

d2 = (
    ('X', 'X', 'O', 'X', 'X', 'X', 'O'),
    ('O', 'O', 'X', 'O', 'O', 'X', 'O'),
    ('O', 'X', 'O', 'X', 'X', 'O', 'O'),
    ('O', 'O', 'X', 'X', 'X', 'O', 'X'),
    ('X', 'X', 'O', 'O', 'X', 'X', 'O'),
    ('O', 'O', 'O', 'X', 'O', 'X', 'O')
    )

# print(check_winner(game_board))
print(check_winner(xwins))
print(check_winner(owins))
print(check_winner(nowins))

# print (xwins[5][0])
# print (xwins[5][1])
# print (xwins[len(xwins)-1][0])
# print (xwins[len(xwins)-1][1])
print('--------------------------')
print(check_winner(v_x))
print(check_winner(h_o))
print(check_winner(d_x1))
print(check_winner(d2))