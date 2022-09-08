import random
import sys


matrix = []
matrix_size = 0
mine_count = 0
open_cells = []

numbers = {}
numbers[0] = "\x1b[6;30;42m 0️ "
numbers[1] = "\x1b[6;30;44m 1 "
numbers[2] = "\x1b[6;30;44m 2 "
numbers[3] = "\x1b[6;30;43m 3 "
numbers[4] = "\x1b[6;30;43m 4 "
numbers[5] = "\x1b[6;30;45m 5 "
numbers[6] = "\x1b[6;30;45m 6 "
numbers[7] = "\x1b[5;37;41m 7 "
numbers[8] = "\x1b[5;37;41m 8 "


class MessageType(object):
    # White Text + Red Background
    ERROR = "\x1b[1;37;41m"
    # White Text + Blue Background
    TITLE = "\x1b[1;37;44m"
    # White Text + Green Background
    SUCCESS = "\x1b[1;37;42m"
    # White Text + Yellow Background
    INFO = "\x1b[1;30;43m"


def create_random_mines():
    mine_counter = mine_count
    matrix_area = matrix_size*matrix_size
    mine_list = []
    while mine_counter != 0:
        random_number = random.randrange(matrix_area)
        if random_number not in mine_list:
            mine_list.append(random_number)
            mine_counter -= 1
    return mine_list


def is_in_matrix(x, y):
    if (x < matrix_size and x >= 0) and (y < matrix_size and y >= 0):
        return True
    else:
        return False


def is_there_a_mine(x, y):
    if matrix[x][y] == "x":
        return True
    else:
        return False


def add_one_around(x, y):
    # left
    direction_x = x-1
    if is_in_matrix(direction_x, y):
        if not is_there_a_mine(direction_x, y):
            matrix[direction_x][y] += 1
    # right
    direction_x = x+1
    if is_in_matrix(direction_x, y):
        if not is_there_a_mine(direction_x, y):
            matrix[direction_x][y] += 1
    # down
    direction_y = y-1
    if is_in_matrix(x, direction_y):
        if not is_there_a_mine(x, direction_y):
            matrix[x][direction_y] += 1
    # up
    direction_y = y+1
    if is_in_matrix(x, direction_y):
        if not is_there_a_mine(x, direction_y):
            matrix[x][direction_y] += 1
    # down left
    direction_x = x-1
    direction_y = y-1
    if is_in_matrix(direction_x, direction_y):
        if not is_there_a_mine(direction_x, direction_y):
            matrix[direction_x][direction_y] += 1
    # up right
    direction_x = x+1
    direction_y = y+1
    if is_in_matrix(direction_x, direction_y):
        if not is_there_a_mine(direction_x, direction_y):
            matrix[direction_x][direction_y] += 1
    # down right
    direction_x = x+1
    direction_y = y-1
    if is_in_matrix(direction_x, direction_y):
        if not is_there_a_mine(direction_x, direction_y):
            matrix[direction_x][direction_y] += 1
    # up left
    direction_x = x-1
    direction_y = y+1
    if is_in_matrix(direction_x, direction_y):
        if not is_there_a_mine(direction_x, direction_y):
            matrix[direction_x][direction_y] += 1


def create_minefield():
    line = []
    mine_list = create_random_mines()
    counter = 0
    for y in range(matrix_size):
        for x in range(matrix_size):
            if counter in mine_list:
                line.append("x")
            else:
                line.append(0)
            counter = counter+1
        matrix.append(line)
        line = []


def add_mine_counts():
    counter = 0
    for x in range(matrix_size):
        for y in range(matrix_size):
            counter = counter+1
            if matrix[x][y] == "x":
                add_one_around(x, y)


def print_minefield(all_open=False):
    print()
    print_message("{0:{1}{2}{3}}".format(
        'MINESWEEPER', ' ', '>', (matrix_size+5)*2)+matrix_size*2*" ", MessageType.TITLE)
    print()
    row = "       "
    for i in range(matrix_size):
        row = row + " {0:<3}".format(str(i+1))
    print(row)
    for y in range(matrix_size):
        row = "      ┏"
        if y == 0:
            for m in range(matrix_size-1):
                row = row + "━━━┳"
            print(row+"━━━┓")
        row = "  {0: <2}  ".format(str(y+1))
        for x in range(matrix_size):
            mine_cell = "\x1b[5;37;40m @ "
            if len(open_cells) > 0:
                if [x, y] in open_cells or all_open:
                    if matrix[x][y] == "x":
                        mine_cell = "\x1b[0;30;41m💣'"
                    else:
                        mine_cell = numbers[matrix[x][y]]
            row = row + "┃" + str(mine_cell) + "\x1b[0m"
        print(row + "┃")
        if y == matrix_size-1:
            row = "      ┗"
            for x in range(matrix_size-1):
                row = row + "━━━┻"
            print(row+"━━━┛")
        else:
            row = "      ┣━━━"
            for x in range(matrix_size-1):
                row = row + "╋━━━"
            print(row + '┫')
    print()


def play(x, y):
    if is_there_a_mine(x, y):
        print_message("BOOOM!")
        print()
        print_message("YOU LOST!!!!")
        return True
    else:
        print_message("Good!", MessageType.SUCCESS)
        print()
        return False


def clean_screen():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')


def is_valid_selection(selected_column, selected_row):
    if selected_column and selected_column.isnumeric() and selected_row and selected_row.isnumeric():
        return True
    else:
        print_message("Selected Column/Row is not valid!")
        return False


def print_message(message, message_type=MessageType.ERROR):
    print(message_type+" "+len(message)*" "+" \x1b[0m")
    print(message_type+" {} \x1b[0m".format(message))
    print(message_type+" "+len(message)*" "+" \x1b[0m")


def run_game():
    clean_screen()
    create_minefield()
    add_mine_counts()
    print_minefield()
    while(True):
        if len(open_cells) == (matrix_size*matrix_size-mine_count):
            print_message("YOU WIN!!!!", MessageType.SUCCESS)
            print_minefield(True)
            exit()
        try:
            selected_column = input("Column : ")
            selected_row = input("Row    : ")
        except KeyboardInterrupt:
            exit()
        if is_valid_selection(selected_column, selected_row):
            selected_column = int(selected_column)-1
            selected_row = int(selected_row)-1
            if is_in_matrix(selected_column, selected_row):
                clean_screen()
                selected_cell = [selected_column, selected_row]
                if selected_cell in open_cells:
                    print_message("This cell is already opened!")
                else:
                    open_cells.append(selected_cell)
                    if play(selected_column, selected_row):
                        break
                print_minefield()
                print()
                print_message("Press CTRL + C to exit.", MessageType.INFO)
                print()
            else:
                print_message("Selected cell is not in range!")
    print_minefield(True)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        matrix_size = int(sys.argv[1])
        mine_count = int(sys.argv[2])
        if mine_count >= (matrix_size*matrix_size):
            print_message(
                "ERROR: Mine count must be lesser than the available cell count!")
            exit()
        run_game()
    else:
        print_message("Command Line MINESWEEPER GAME", MessageType.TITLE)
        print_message("USAGE   : python3 {} <size> <mine_count>".format(
            sys.argv[0]), MessageType.INFO)
        print_message("EXAMPLE : python3 {} 6 5".format(
            sys.argv[0]), MessageType.SUCCESS)
        print()
        print_message("Starting default 5x5 board with 5 mines",
                      MessageType.SUCCESS)
        input("Press Enter to continue...")
        matrix_size = 5
        mine_count = 5
        run_game()
