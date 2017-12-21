class Program:
    name = ""
    weight = 0
    children = []

    def __init__(self, inputString):
        dataArray = inputString.translate(None, ',()->').split()
        self.name = dataArray[0]
        self.weight = int(dataArray[1])
        if len(dataArray) > 2:
            self.children = dataArray[2:len(dataArray)]

    def __str__(self):
         return "[" + self.name + " " + str(self.weight) + "]"

    def is_parent_of(self, candidate):
        return candidate in self.children

programs = map(Program, open("input").read().splitlines())

def findRoot(programs, currentProgram):
    index = 0
    while (index < len(programs)):
        if programs[index].is_parent_of(currentProgram.name):
            return findRoot(programs, programs[index])
        index = index + 1

    return currentProgram

def findProgramByName(programs, name):
    index = 0
    while (index < len(programs)):
        if programs[index].name == name:
            return programs[index]
        index = index + 1
    print "Not found!"
    return None

def findWeight(programs, currentProgram):
    weight = currentProgram.weight
    index = 0
    while (index < len(currentProgram.children)):
        currentChild = findProgramByName(programs, currentProgram.children[index])
        childWeight = findWeight(programs, currentChild)
        weight = weight + childWeight
        index = index + 1
    return weight

def findUnbalancedChild(programs, currentProgram, requiredWeight):
    cI = 0
    children = []
    childWeights = []
    while (cI < len(currentProgram.children)):
        child = findProgramByName(programs, currentProgram.children[cI])
        children.append(child)
        childWeights.append(findWeight(programs, child))
        cI = cI + 1
    if len(children) > 1 and childWeights.count(childWeights[0]) != len(childWeights):
        print currentProgram.name + " is unbalanced"
        minCount = childWeights.count(min(childWeights))
        maxCount = childWeights.count(max(childWeights))
        if minCount > maxCount:
            nextProg = children[childWeights.index(max(childWeights))]
            targetWeight = min(childWeights)
        else:
            nextProg = children[childWeights.index(min(childWeights))]
            targetWeight = max(childWeights)
        print "Proceeding to " + nextProg.name
        findUnbalancedChild(programs, nextProg, targetWeight)

    else:
        actualWeight = findWeight(programs, currentProgram)
        print currentProgram.name + " is balanced!"
        print "Required val is " + str(requiredWeight)
        print "Actual val is " + str(actualWeight)
        print "Current program weight is " + str(currentProgram.weight)
        answer = currentProgram.weight + requiredWeight - actualWeight
        print "Current program weight should be " + str(answer)
        return currentProgram



root = findRoot(programs, programs[0])

findUnbalancedChild(programs, root, 0)
