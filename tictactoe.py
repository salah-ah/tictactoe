row_one = [' '] * 3
row_two = [' '] * 3
row_three = [' '] * 3


# A function to format the grid
def display_grid(rw_1, rw_2, rw_3):
    row_1 = f'| {rw_1[0]} {rw_1[1]} {rw_1[2]} |'
    row_2 = f'| {rw_2[0]} {rw_2[1]} {rw_2[2]} |'
    row_3 = f'| {rw_3[0]} {rw_3[1]} {rw_3[2]} |'

    print('---------')
    print(row_1)
    print(row_2)
    print(row_3)
    print('---------')


# A function to check if the chosen cell is empty or not
def check_cell(row, idx):
    if row[idx] == "X" or row[idx] == "O":
        print("This cell is occupied! Choose another one!")
        return False
    return True


# A function to swap the players
def swap_player(plyr, plyr_x, plyr_o):
    if plyr == plyr_x:
        return plyr_o

    return plyr_x


# A function to check the winner
def check_winner(char):
    if check_rows(char) or check_cols(char) or check_diagonals(char):
        return True
    return False


# Checking the rows
def check_rows(char):
    if (row_one[0] == row_one[1] == row_one[2] == char) \
            or (row_two[0] == row_two[1] == row_two[2] == char) \
            or (row_three[0] == row_three[1] == row_three[2] == char):
        return True


# Checking the cols
def check_cols(char):
    if (row_one[0] == row_two[0] == row_three[0] == char) \
            or (row_one[1] == row_two[1] == row_three[1] == char) \
            or (row_one[2] == row_two[2] == row_three[2] == char):
        return True


# Checking the diagonals
def check_diagonals(char):
    if (row_one[0] == row_two[1] == row_three[2] == char) \
            or (row_three[0] == row_two[1] == row_one[2] == char):
        return True


def play():
    player_x = 'X'
    player_o = 'O'
    current_player = player_x
    empty_cell = 9
    is_playing = True
    
    while is_playing:
        # Getting the coordinates from the current_player
        display_grid(row_one, row_two, row_three)
        coords = input("Enter the coordinates: ").split()

        if not coords[0].isdigit() or not coords[1].isdigit():
            print("You should enter numbers!")
            continue

        elif coords[0] not in '123' or coords[1] not in '123':
            print("Coordinates should be from 1 to 3!")
            continue

        else:
            row_number = int(coords[0])
            y = int(coords[1]) - 1

            # Checking if the chosen cell is empty and assign the current_player
            if row_number == 1 and check_cell(row_one, y):
                row_one[y] = current_player
                empty_cell -= 1

            elif row_number == 2 and check_cell(row_two, y):
                row_two[y] = current_player
                empty_cell -= 1

            elif row_number == 3 and check_cell(row_three, y):
                row_three[y] = current_player
                empty_cell -= 1

            # Checking for the winner
            if check_winner(player_x):
                display_grid(row_one, row_two, row_three)
                print('X wins')
                is_playing = False
            elif check_winner(player_o):
                display_grid(row_one, row_two, row_three)
                print('O wins')
                is_playing = False

            # Checking for draw
            if empty_cell == 0 and is_playing:
                display_grid(row_one, row_two, row_three)
                print('Draw')
                is_playing = False

            # Swapping the current_player
            current_player = swap_player(current_player, player_x, player_o)


play()
