
import pygame

pygame.font.init()

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacTo')

X_O_FONT = pygame.font.SysFont('comicsans', 100)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_window(spaces, spaces2, letters):
    WIN.fill(WHITE)
    for space in spaces:
        pygame.draw.rect(WIN, BLACK, space)

    i = 0
    for space in spaces2:
        pygame.draw.rect(WIN, WHITE, space)
        space_text = X_O_FONT.render(letters[i], True, BLACK)
        WIN.blit(space_text, (space.x + 35, space.y + 5))
        i += 1

    pygame.display.update()


def player_1_place(keys_pressed, letters, player_1_letter):
    if keys_pressed[pygame.K_1] and letters[8] == '':
        letters[8] = player_1_letter

    if keys_pressed[pygame.K_2] and letters[7] == '':
        letters[7] = player_1_letter

    if keys_pressed[pygame.K_3] and letters[6] == '':
        letters[6] = player_1_letter

    if keys_pressed[pygame.K_4] and letters[5] == '':
        letters[5] = player_1_letter

    if keys_pressed[pygame.K_5] and letters[4] == '':
        letters[4] = player_1_letter

    if keys_pressed[pygame.K_6] and letters[3] == '':
        letters[3] = player_1_letter

    if keys_pressed[pygame.K_7] and letters[2] == '':
        letters[2] = player_1_letter

    if keys_pressed[pygame.K_8] and letters[1] == '':
        letters[1] = player_1_letter

    if keys_pressed[pygame.K_9] and letters[0] == '':
        letters[0] = player_1_letter

    return letters


def player_2_place(keys_pressed, letters, player_2_letter):
    if keys_pressed[pygame.K_1] and letters[8] == '':
        letters[8] = player_2_letter

    if keys_pressed[pygame.K_2] and letters[7] == '':
        letters[7] = player_2_letter

    if keys_pressed[pygame.K_3] and letters[6] == '':
        letters[6] = player_2_letter

    if keys_pressed[pygame.K_4] and letters[5] == '':
        letters[5] = player_2_letter

    if keys_pressed[pygame.K_5] and letters[4] == '':
        letters[4] = player_2_letter

    if keys_pressed[pygame.K_6] and letters[3] == '':
        letters[3] = player_2_letter

    if keys_pressed[pygame.K_7] and letters[2] == '':
        letters[2] = player_2_letter

    if keys_pressed[pygame.K_8] and letters[1] == '':
        letters[1] = player_2_letter

    if keys_pressed[pygame.K_9] and letters[0] == '':
        letters[0] = player_2_letter

    return letters


def main_f():
    # DEFINE ALL MAIN VARIABLES

    spaces = []
    spaces2 = []
    letters = ['', '', '', '', '', '', '', '', '']
    temp_x = WIDTH/4
    temp_y = 10
    space_width = 160
    space_height = 160

    turn = ''

    player_1_letter = 'x'
    player_2_letter = 'y'

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
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if not run:
            break

        keys_pressed = pygame.key.get_pressed()
        letters = player_1_place(keys_pressed, letters, player_1_letter)
        letters = player_2_place(keys_pressed, letters, player_2_letter)

        draw_window(spaces, spaces2, letters)


main_f()
