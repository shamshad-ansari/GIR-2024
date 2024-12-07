# The size of the board!
size = 3

# Set up board data
board = []
for i in range(size):
  board.append([])
  for j in range(size):
    board[i] += '-'

# Set up player info
player_num = 1
player_symbol = 'X'
winner = None

# Start game loop
for i in range(size ** 2):
    # Get location from user and update board variable
    valid = False
    while not valid:
        # Assume we'll get a valid input
        valid = True

        # Get input from user
        loc = input(f'Player {player_num}, enter the number representing the location to place your {player_symbol} (x,y): ')

        # Update the variable representing the location if not already set
        position = loc.split(',')

        if len(position) != 2:
            valid = False
        else:
            x = int(position[0])
            y = int(position[1])

            if x < size and y < size and board[x][y] == '-':
                board[x][y] = player_symbol
            else:
                valid = False

        if valid == False:
            print('That is not a valid input, try again')

    # Add a blank line to space things out
    print()

    # Display the current state of the
    print('Here is the state of the board:')
    for row in board:
      print(' '.join(row))

    # Check if any of the possible lines are all the same non-empty value

    # Check each horizontal line
    for row in board:
        if(row[0] != '-' and all(i == row[0] for i in row)):
            winner = player_symbol

    # Check each vertical
    for col in range(size):
        if all(board[row][col] == player_symbol for row in range(size)):
            winner = player_symbol

    # Check diagonals
    count = 0
    for i in range(size):
        if board[i][i] == player_symbol:
            count += 1
    if count == size:
      winner = player_symbol

    count = 0
    for i in range(size):
        if board[i][size - 1 - i] == player_symbol:
            count += 1
    if count == size:
      winner = player_symbol


    # If there is a winner, say who and stop the game loop
    if winner:
        if (winner == 'X'):
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')
        break

    # Add a blank line to space things out
    print()

    # Toggle current player
    if player_symbol == 'X':
        player_symbol = 'O'
        player_num = 2
    else:
        player_symbol = 'X'
        player_num = 1

if not winner:
    print('Tied game!')
