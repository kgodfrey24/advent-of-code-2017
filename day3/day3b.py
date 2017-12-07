def printMatrix(matrix):
    yIdx = 0
    while yIdx < len(matrix):
        xIdx = 0
        string = ""
        while xIdx < len(matrix):
            string = string + "\t" + str(matrix[xIdx][yIdx])
            xIdx = xIdx + 1
        print string

        yIdx = yIdx + 1

def printCoords(x, y):
    print "x: ",x," y: ",y

def determineValue(m, x, y):
    if (m[x][y] != 0):
        print "Error!"
        printMatrix(m)
        exit()
    return m[x-1][y+1] + m[x][y+1] + m[x+1][y+1] + m[x-1][y] + m[x+1][y] + m[x-1][y-1] + m[x][y-1] + m[x+1][y-1]


w, h = 15, 15;
matrix = [[0 for y in range(h)] for x in range(w)]

x = 7
y = 7

sideWidth = 3

matrix[x][y] = 1
printMatrix(matrix)

x = x + 1
while sideWidth < 10:
    # steps up
    stepsUp = sideWidth - 2
    print "Steps Up: ",stepsUp
    stepsMade = 0
    while (stepsMade < stepsUp):
        matrix[x][y] = determineValue(matrix, x, y)
        y = y - 1
        stepsMade = stepsMade + 1

    # steps left
    stepsLeft = sideWidth - 1
    print "Steps Left: ",
    printCoords(x,y)
    stepsMade = 0
    while (stepsMade < stepsLeft):
        matrix[x][y] = determineValue(matrix, x, y)
        x = x - 1
        stepsMade = stepsMade + 1

    # steps down
    stepsDown = sideWidth - 1
    print "Steps Down: ",stepsDown
    stepsMade = 0
    while (stepsMade < stepsDown):
        matrix[x][y] = determineValue(matrix, x, y)
        y = y + 1
        stepsMade = stepsMade + 1

    # steps right
    stepsRight = sideWidth
    print "Steps Right: ",stepsRight
    stepsMade = 0
    while (stepsMade < stepsRight):
        matrix[x][y] = determineValue(matrix, x, y)
        x = x + 1
        stepsMade = stepsMade + 1

    printMatrix(matrix)

    sideWidth = sideWidth + 2
