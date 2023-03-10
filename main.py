import turtle as t

t.speed(0)
t.hideturtle()
t.penup()
t.setpos(-200, -200)

def playfield_init():
    with open("feld.txt") as file:
        lines = file.readlines()
        playfield1 = [[int(c) for c in line.strip()] for line in lines]
    return playfield1

def count_living(playfield, i, j):
    num_rows = len(playfield)
    num_cols = len(playfield[0])
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni = (i + di) % num_rows
            nj = (j + dj) % num_cols
            if playfield[ni][nj] == 1:
                count += 1
    return count

def check_rules(playfield1):
    num_rows = len(playfield1)
    num_cols = len(playfield1[0])
    playfield2 = [[0 for j in range(num_cols)] for i in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            count = count_living(playfield1, i, j)
            if playfield1[i][j] == 1 and (count < 2 or count > 3):
                playfield2[i][j] = 0
            elif playfield1[i][j] == 0 and count == 3:
                playfield2[i][j] = 1
            else:
                playfield2[i][j] = playfield1[i][j]
    return playfield2

def playfield_swap(playfield1, playfield2):
    for i in range(len(playfield2)):
        for j in range(len(playfield2[0])):
            playfield1[i][j] = playfield2[i][j]

                
def playfield_draw(playfield):
    for i in range(len(playfield)):
        for j in range(len(playfield[0])):
            try:
                t.penup()
                t.goto(j * 30, -i * 30)

                if playfield[i][j] == 1:
                    t.dot(25, "black")
                t.forward(5)
                
            except:
                exit()

def main():
    playfield1 = playfield_init()
    while True:
        playfield2 = check_rules(playfield1)
        playfield_swap(playfield1, playfield2)
        playfield_draw(playfield1)
        playfield1 = playfield2
        t.clear()
        t.update()

if __name__ == "__main__":
    main()
