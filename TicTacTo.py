
import pygame
import random

pygame.font.init()

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacTo')

FPS = 60

X_O_FONT = pygame.font.SysFont('comicsans', 100)
WINNER_FONT = pygame.font.SysFont('comicsans', 50)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def draw_window(spaces, spaces2, letters, turn):
    WIN.fill(WHITE)
    for space in spaces:
        pygame.draw.rect(WIN, BLACK, space)

    i = 0
    for space in spaces2:
        pygame.draw.rect(WIN, WHITE, space)
        space_text = X_O_FONT.render(letters[i], True, BLACK)
        WIN.blit(space_text, (space.x + 35, space.y + 5))
        i += 1

    turn_text = X_O_FONT.render(str(turn), True, BLACK)
    WIN.blit(turn_text, (20, 0))

    pygame.display.update()


def draw_winner(winner):
    winner_text = WINNER_FONT.render(str(winner), True, RED)
    WIN.blit(winner_text, (WIDTH/2 - winner_text.get_width() / 2, HEIGHT/2 - winner_text.get_height()))

    pygame.display.update()
    pygame.time.delay(3000)


def player_1_place(keys_pressed, letters, player_1_letter, turn):
    if turn == 0:
        next_turn = 0
        if keys_pressed[pygame.K_c] and letters[8] == '':
            letters[8] = player_1_letter
            next_turn = 1

        if keys_pressed[pygame.K_x] and letters[7] == '':
            letters[7] = player_1_letter
            next_turn = 1

        if keys_pressed[pygame.K_z] and letters[6] == '':
            letters[6] = player_1_letter
            next_turn = 1

        if keys_pressed[pygame.K_d] and letters[5] == '':
            letters[5] = player_1_letter
            next_turn = 1

        if keys_pressed[pygame.K_s] and letters[4] == '':
            letters[4] = player_1_letter
            next_turn = 1

        if keys_pressed[pygame.K_a] and letters[3] == '':
            letters[3] = player_1_letter
            next_turn = 1

        if keys_pressed[pygame.K_e] and letters[2] == '':
            letters[2] = player_1_letter
            next_turn = 1

        if keys_pressed[pygame.K_w] and letters[1] == '':
            letters[1] = player_1_letter
            next_turn = 1

        if keys_pressed[pygame.K_q] and letters[0] == '':
            letters[0] = player_1_letter
            next_turn = 1

        if next_turn == 1:
            turn = 1

    return [letters, turn]


def player_2_place(keys_pressed, letters, player_2_letter, turn):
    if turn == 1:
        next_turn = 0
        if keys_pressed[pygame.K_KP3] and letters[8] == '':
            letters[8] = player_2_letter
            next_turn = 1

        if keys_pressed[pygame.K_KP2] and letters[7] == '':
            letters[7] = player_2_letter
            next_turn = 1

        if keys_pressed[pygame.K_KP1] and letters[6] == '':
            letters[6] = player_2_letter
            next_turn = 1

        if keys_pressed[pygame.K_KP6] and letters[5] == '':
            letters[5] = player_2_letter
            next_turn = 1

        if keys_pressed[pygame.K_KP5] and letters[4] == '':
            letters[4] = player_2_letter
            next_turn = 1

        if keys_pressed[pygame.K_KP4] and letters[3] == '':
            letters[3] = player_2_letter
            next_turn = 1

        if keys_pressed[pygame.K_KP9] and letters[2] == '':
            letters[2] = player_2_letter
            next_turn = 1

        if keys_pressed[pygame.K_KP8] and letters[1] == '':
            letters[1] = player_2_letter
            next_turn = 1

        if keys_pressed[pygame.K_KP7] and letters[0] == '':
            letters[0] = player_2_letter
            next_turn = 1

        if next_turn == 1:
            turn = 0
    return [letters, turn]


def check_win(board, letter):
    if board[0] == letter and board[1] == letter and board[2] == letter:
        return True
    if board[3] == letter and board[4] == letter and board[5] == letter:
        return True
    if board[6] == letter and board[7] == letter and board[8] == letter:
        return True

    if board[0] == letter and board[3] == letter and board[6] == letter:
        return True
    if board[1] == letter and board[4] == letter and board[7] == letter:
        return True
    if board[2] == letter and board[5] == letter and board[8] == letter:
        return True

    if board[0] == letter and board[4] == letter and board[8] == letter:
        return True
    if board[2] == letter and board[4] == letter and board[6] == letter:
        return True

    return False


def check_tie(board):
    not_empty = 0
    for i in board:
        if i != '':
            not_empty += 1

    if not_empty == len(board):
        return True
    return False


def main_f():
    # DEFINE ALL MAIN VARIABLES

    spaces = []
    spaces2 = []
    letters = ['', '', '', '', '', '', '', '', '']
    winner = ''
    temp_x = WIDTH/4
    temp_y = 10
    space_width = 160
    space_height = 160

    turn = random.randint(0, 1)

    print(turn)

    player_1_letter = 'X'
    player_2_letter = 'O'

    temp_row = 1
    for i in range(9):
        spaces.append(pygame.Rect(temp_x, temp_y, space_width, space_height))
        spaces2.append(pygame.Rect(temp_x + 5, temp_y + 5, space_width - 10, space_height - 10))
        if temp_row == 3:
            temp_x = WIDTH/4
            temp_y += space_height
            temp_row = 0
        else:
            temp_x += space_width
        temp_row += 1

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not run:
            break

        keys_pressed = pygame.key.get_pressed()
        letters, turn = player_1_place(keys_pressed, letters, player_1_letter, turn)
        letters, turn = player_2_place(keys_pressed, letters, player_2_letter, turn)

        draw_window(spaces, spaces2, letters, turn)

        if check_win(letters, player_1_letter):
            winner = 'The winner is Player 1!'
            break
        if check_win(letters, player_2_letter):
            winner = 'The winner is Player 2!'
            break
        if check_tie(letters):
            winner = 'It\'s a Tie!'
            break

    if winner != '':
        draw_winner(winner)
        main_f()


main_f()
