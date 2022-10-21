# X-O Game

#
# Form a game board a show it.
# Argument {field} is a list of 3-character strings,
# representing 3 by 3 game field.
#
def show_game_field(field):
    great_field = [
        ' |123',
        '-+---',
        '1|...',
        '2|...',
        '3|...',
    ]

    great_field[2] = great_field[2][0:2] + game_field[0]
    great_field[3] = great_field[3][0:2] + game_field[1]
    great_field[4] = great_field[4][0:2] + game_field[2]

    for row in great_field:
        print(row)

# End of function show_game_field()

#
# Obtain coordinates column and row.
# Both the coordinated are between 1 and 3 including.
# Returns a list [column, row].
# Function argument {character} is supposed to be either 'x' or '0',
# only needed for the input prompt.
#
def get_coordinates(character):
    if not (character == 'x' or character == '0'):
        print(f"FATAL: get_coordinates: bad character {character}.")
        print("Must be either x or 0.")
        print("Aborting...")
        exit(1)

    while True:
        coordinates = input(f"Where to put your {character} (column and row, 1 to 3).\n").split()

        if len(coordinates) != 2:
            print("ERROR: get_coordinates: wrong format. Must be two numbers from 1 to 3")
            continue

        [column, row] = map(int, coordinates)
        # print(column, row)

        if not column in range(1, 4):
            print("ERROR: get_coordinates: wrong format. Column must be between 1 and 3 (including)")
            continue

        if not row in range(1, 4):
            print("ERROR: get_coordinates: wrong format. Row must be between 1 and 3 (including)")
            continue

        return [column, row]

# End of function get_coordinates()

#
# Check if winning situation.
# Return True if it is, otherwise False.
# Argument {field} is a list of 3-character strings,
# representing 3 by 3 game field.
# {character} must be in all winning positions.
#
def check_if_won(field, character):
    all_lists_to_check = []

    # 3 rows
    all_lists_to_check.append(field[0])
    all_lists_to_check.append(field[1])
    all_lists_to_check.append(field[2])

    # 3 columns
    all_lists_to_check.append(field[0][0] + field[1][0] + field[2][0])
    all_lists_to_check.append(field[0][1] + field[1][1] + field[2][1])
    all_lists_to_check.append(field[0][2] + field[1][2] + field[2][2])

    # two diagonals
    all_lists_to_check.append(field[0][0] + field[1][1] + field[2][2])
    all_lists_to_check.append(field[0][2] + field[1][1] + field[2][0])

    return any([a_list == character*3 for a_list in all_lists_to_check])

# End of function check_if_won

#
# Create a new line by placing {character} to position {pos}.
# Returns new line.
# Arguments:
# {L} - template line
# {pos} - position, counting from 0
# {character} - this is what is placed on position
#
def make_line(L, pos, character):
    if not pos in range(len(L)):
        print(f"ERROR: make_line: {pos} is out of range")
        exit(1)

    new_line = ''
    for i in range(len(L)):
        if i == pos:
            new_line += character
        else:
            new_line += L[i]

    return new_line
# End of make_line

#
# Check if position {pos} in string {a_line} is already used -
# that is the character is this position is anything other than {char_background}.
# Return True if already used.
#
def check_if_used(a_line, pos, char_background):
    if a_line[pos] == char_background:
        return False # position is not used
    else:
        return True # position is used
# End of check_if_used

# Main

#
# One game iteration.
# Argument:
# {character} is either 'x' or '0'
#
def do_one_iteration(character):
    global game_field  # let's try global var for fun

    while True:
        [column, row] = get_coordinates(character)
        if check_if_used(game_field[row-1], column-1, '.'):
            print("This position is already used. Enter new one.")
            continue
        else:
            break

    game_field[row-1] = make_line(game_field[row-1], column-1, character)
    show_game_field(game_field)
    if check_if_won(game_field, character):
        print(f"Player 1 ({character}) wins")
        exit(0)
# End of do_one_iteration

# True if game still can be played.
# {field}  - game board
# {character} - background character
def game_playable(field, character):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == character:
                return True
    return False
# The code below in more Pythonic, but does not work. No time to debug.
#        if any([field[row][col] == character for col in range(len(field[row]))]):
#            return True
#        return False
# End of game_playable


game_field = [
    '...',
    '...',
    '...'
]

show_game_field(game_field)

while True:
    if game_playable(game_field, '.'):
        do_one_iteration('x')
    else:
        break

    if game_playable(game_field, '.'):
        do_one_iteration('0')
    else:
        break

# End of File
