import pygame
import random
import math

size = int(input("Größe des Spielfeldes: "))
length = round(math.sqrt(size))

with open("feld.txt", "w") as file:
    for i in range(length):
        row = "".join([str(random.randint(0, 1)) for _ in range(length)])
        file.write(row + "\n")

pygame.init()

# Set up the screen size
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
dot_size = int(min(screen_width / length, screen_height / length))
screen = pygame.display.set_mode((dot_size * length, dot_size * length))

# Set up the colors
BLACK = (255, 255, 0)
WHITE = (0, 0, 0)

# Set up the game variables
current_pos = 0

def playfield_init():
    global rect
    with open("feld.txt") as file:
        lines = file.readlines()
        rect = [[int(c) for c in line.strip()] for line in lines]

def playfield_swap():
    global rect
    with open("feld.txt", "w") as file:
        for line in rect:
            file.write("".join(str(c) for c in line) + "\n")

def count_living(rect):  #zählt die überlebenden Nachbarn
    global current_pos, count
    num_rows = len(rect)
    num_cols = len(rect[0])
    i, j = divmod(current_pos, num_cols)
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni = (i + di) % num_rows
            nj = (j + dj) % num_cols
            if rect[ni][nj] == 1:
                count += 1
    current_pos += 1
    return current_pos, rect

def check_rules(rect,current_pos , count):
    i, j = divmod(current_pos, len(rect[0]))
    try:
        if rect[i][j] == 1 and (count < 2 or count > 3):
            rect[i][j] = 0
        elif rect[i][j] == 0 and count == 3:
            rect[i][j] = 1
    except:
        ()

def playfield_draw():
    for i, row in enumerate(rect):
        for j, val in enumerate(row):
            if val == 1:
                pygame.draw.rect(screen, BLACK, (j * dot_size, i * dot_size, dot_size, dot_size))
            else:
                pygame.draw.rect(screen, WHITE, (j * dot_size, i * dot_size, dot_size, dot_size))

def main():
    playfield_init()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill(WHITE)
        playfield_draw("feld.txt")
        pygame.display.flip()

        # Calculate next state
        next_rect = [[0] * length for _ in range(length)]
        for i in range(length):
            for j in range(length):
                count = count_living(rect, i, j)
                check_rules(rect, next_rect, i, j, count)

        # Update playfield
        rect = next_rect
        playfield_swap()
        playfield_draw("feld.txt")

        # Wait for next tick
        clock.tick(60)


if __name__ == '__main__':
    main()
