class Instruction:
    def __init__(self, inputString):
        array = inputString.split()
        self.register = array[0]
        self.op = array[1]
        self.constant = int(array[2])
        self.comparativeRegister = array[4]
        self.condition = array[5]
        self.comparativeConstant = int(array[6])

instructions = map(Instruction, open("input").read().splitlines())
registers = {}

def evalulateCondition(c1, c2, condition):
    if condition == "==":
        return c1 == c2
    elif condition == "!=":
        return c1 != c2
    elif condition == ">=":
        return c1 >= c2
    elif condition == ">":
        return c1 > c2
    elif condition == "<":
        return c1 < c2
    elif condition == "<=":
        return c1 <= c2
    else:
        print "Something has gone wrong with " + condition
        exit()

maxValue = 0
for i in instructions:
    comparativeRegister = registers.get(i.comparativeRegister, 0)
    shouldPerformOp = evalulateCondition(comparativeRegister, i.comparativeConstant, i.condition)
    if (shouldPerformOp):
        if i.op == "inc":
            registers[i.register] = registers.get(i.register, 0) + i.constant
        elif i.op == "dec":
            registers[i.register] = registers.get(i.register, 0) - i.constant

    currentMaxValue = registers[max(registers, key=registers.get)]
    if (currentMaxValue > maxValue):
        maxValue = currentMaxValue

print maxValue
