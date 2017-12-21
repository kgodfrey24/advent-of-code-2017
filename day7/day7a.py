

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
            print "Found parent for " + currentProgram.name + " it is " + programs[index].name
            return findRoot(programs, programs[index])
        index = index + 1

    return "No Parent for " + currentProgram.name

print findRoot(programs, programs[0])
