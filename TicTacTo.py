
import pygame

pygame.font.init()

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacTo')

X_O_FONT = pygame.font.SysFont('comicsans', 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_window(spaces, spaces2, letters):
    WIN.fill(WHITE)
    for space in spaces:
        pygame.draw.rect(WIN, BLACK, space)

    for space in spaces2:
        pygame.draw.rect(WIN, WHITE, space)

    pygame.display.update()


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

        draw_window(spaces, spaces2, letters)


main_f()
