import turtle as t
t.color('black')
t.speed(1)

def playfield_init():
    y=0
    with open('feld.txt') as file:
        lines = [line.strip() for line in file.readlines()]
    matrix = []
    for line in lines:
        x=len(line)
        row = []
        y+=1
        for char in line:
            row.append(int(char))
        matrix.append(row)
    #print(matrix)
    return matrix, x, y
    
    
#def playfield_read():
    
#def playfield_swap():
    
def count_living(matrix,x,y,a,b,living):
    #zählt die überlebenden Nachbarn
    
    if (matrix[i][j] == 1) and (str(a)+str(b)) != (str(i)+str(j)):
        living=+1
    return living
                
                
def check_rules(living):
    if living>=2 and living<=3:
        print('Block lebt')
    else:
        print('Block tot')
    return
        
def playfield_draw(matrix,x,y):
    for i in range(y):
        for j in range(x):
            if matrix[i][j] == 1:
                #print('found', int(i)25, int(j)25)
                t.pu()
                t.goto(j*25,i*-25)
                t.pd()
                t.dot(20)
    return
    
    
def main():
    living,a,b=0,0,0
    matrix, x, y = playfield_init()
    playfield_draw(matrix,x,y)
    for i in range(x*y):
        living=count_living(matrix,x,y,a,b,living)
        check_rules(living)
        living=0
        b=+1
        if b==(x-1):
            b=0
            a=+1
    
if __name__ == "__main__":
    main()
