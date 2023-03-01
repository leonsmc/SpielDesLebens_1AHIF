import turtle as t
import random
import math

size = int(input("Größe des Spielfeldes: "))
length = round(math.sqrt(size))

with open("feld.txt", "w") as file:
        for i in range(length):
            row = "".join([str(random.randint(0, 1)) for _ in range(length)])
            file.write(row + "\n")
t.speed(0)
t.hideturtle()
t.penup()
t.setpos(-200, -200)
dot_size = 25
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
def playfield_draw(file_path):
    with open(file_path) as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line.strip()):
                try:
                    t.penup()
                    t.goto(j * 30, -i * 30) # multiply by 30 to account for dot size
                    #if char == "0":
                        #t.dot(25, "white")
                    if char == "1":
                        t.dot(25, "black")
                    t.forward(5) # add a gap of 5 between dots
                except:
                    exit()
def main():
    playfield_init()
    while True:
        playfield_draw("feld.txt")
        while True:
            count_living(rect)
            check_rules(rect, current_pos, count)
            playfield_swap()
            playfield_draw("feld.txt")
            t.clear()
            for _ in range(current_pos):
                check_rules(rect, current_pos, count)
                playfield_swap()
            t.update()

if __name__ == "__main__":
    main()

print(current_pos)