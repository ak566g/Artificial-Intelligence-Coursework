from math import inf as infinity
from random import choice
import platform
import time
import sys
from os import system

# Initialize the parameters
HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


# Define the function to heuristic evaluation of state.
def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0
    return score


# Judges if a specific player wins
def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


# Define the function test judges if the human or computer wins
def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)


# Define the function: each empty cell will be added into cells' list
def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


# Define the function:A move is valid if the chosen cell is empty
def valid_move(x, y):
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


# Set the move on board, if the coordinates are valid
def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


# Define the alpha-beta-pruning function
def alpha_beta_pruning(state, depth, player, alpha, beta):
    if player == COMP:
        best = [-1, -1, alpha]
    else:
        best = [-1, -1, beta]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = alpha_beta_pruning(state, depth - 1, -player, alpha, beta)
        # The move (+1 or -1) on the board is undo and the row, column are collected.
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score
            if alpha >= beta:
                best[2] = beta

        else:
            if score[2] < best[2]:
                best = score
            if beta <= alpha:
                best[2] = alpha
    return best


"""
# Define the minimax function
def minimax(state, depth, player):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value
                
    return best
"""


#  Clears the console
def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


#  Print the board on console
def render(state, c_choice, h_choice):
    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:

        move = alpha_beta_pruning(board, depth, COMP, alpha=-infinity, beta=+infinity)
        #  move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            sys.exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    play_again = 'Y'
    while play_again == 'Y':
        clean()
        h_choice = ''  # X or O
        c_choice = ''  # X or O
        first = ''  # if human is the first

        print('Start a new game.')

        # Human chooses X or O to play
        while h_choice != 'O' and h_choice != 'X':
            try:
                print('')
                h_choice = input('Choose X or O\nChosen: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                sys.exit()
            except (KeyError, ValueError):
                print('Bad choice')

        # Setting computer's choice
        if h_choice == 'X':
            c_choice = 'O'
        else:
            c_choice = 'X'

        # Human may starts first
        clean()
        while first != 'Y' and first != 'N':
            try:
                first = input('First to start?[y/n]: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                sys.exit()
            except (KeyError, ValueError):
                print('Bad choice')

        # Main loop of this game
        while len(empty_cells(board)) > 0 and not game_over(board):
            if first == 'N':
                ai_turn(c_choice, h_choice)
                first = ''

            human_turn(c_choice, h_choice)
            ai_turn(c_choice, h_choice)

        # Game over message
        if wins(board, HUMAN):
            clean()
            print(f'Human turn [{h_choice}]')
            render(board, c_choice, h_choice)
            print('YOU WIN!')
        elif wins(board, COMP):
            clean()
            print(f'Computer turn [{c_choice}]')
            render(board, c_choice, h_choice)
            print('YOU LOSE!')
        else:
            clean()
            render(board, c_choice, h_choice)
            print('DRAW!')

        # Decide whether to play again
        clean()
        play_again = input('Wanna try again ?(y/n) : ').upper()
        if play_again == 'N':
            print("Welcome to your next game.")
            sys.exit()


if __name__ == '__main__':
    main()
