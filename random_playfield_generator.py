import random
import math

size = 20 #int(input("Größe des Spielfeldes: "))
length = round(math.sqrt(size))

with open("feld.txt", "w") as file:
        for i in range(length):
            row = "".join([str(random.randint(0, 1)) for _ in range(length)])
            file.write(row + "\n")
