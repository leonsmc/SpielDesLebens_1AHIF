import turtle as t
import math

t.speed(0)
t.hideturtle()
t.penup()
t.setpos(-200, -200)
dot_size = 25
abfrageposition = 0

def playfield_init():
    global reckteck
    with open("feld.txt") as file:
        lines = file.readlines()
        reckteck = [[int(c) for c in line.strip()] for line in lines]

def playfield_swap():
    global reckteck
    with open("feld.txt", "w") as file:
        for line in reckteck:
            file.write("".join(str(c) for c in line) + "\n")

def count_living(rechteck):
    global abfrageposition, count
    y_achse = len(rechteck)
    x_achse = len(rechteck[0])
    i, j = divmod(abfrageposition, x_achse)
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni = (i + di) % y_achse
            nj = (j + dj) % x_achse
            if rechteck[ni][nj] == 1:
                count += 1
    abfrageposition += 1
    return abfrageposition, rechteck

def check_rules(rechteck,abfrageposition , count):
    i, j = divmod(abfrageposition, len(rechteck[0]))
    try:
        if rechteck[i][j] == 1 and (count < 2 or count > 3):
            rechteck[i][j] = 0
        elif rechteck[i][j] == 0 and count == 3:
            rechteck[i][j] = 1
    except:
        ()
def playfield_draw(dateipfad):
    with open(dateipfad) as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line.strip()):
                try:
                    t.penup()
                    t.goto(j * 30, -i * 30)
                    if char == "1":
                        t.dot(25, "black")
                    t.forward(5)
                except:
                    exit()
def main():
    playfield_init()
    while True:
        playfield_draw("feld.txt")
        while True:
            count_living(reckteck)
            check_rules(reckteck, abfrageposition, count)
            playfield_swap()
            playfield_draw("feld.txt")
            t.clear()
            for _ in range(abfrageposition):
                check_rules(reckteck, abfrageposition, count)
                playfield_swap()
            t.update()

if __name__ == "__main__":
    main()

print(abfrageposition) 

#Fehler zu beheben: Es wird immer nur die eine Position pro durchlauf verändert und dann geprintet
#                   und dann erst beim nächsten durchlauf die nächste position
