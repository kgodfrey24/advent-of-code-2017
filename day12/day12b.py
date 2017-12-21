mappings = map(str.split, open("input").read().translate(None, ',<->').splitlines())

elements = {}
for m in mappings:
    elements[m[0]] = m[1:]

def findGroup(elements, startElement):
    elementsConnectedToStart = [startElement]
    newConnections = True
    while newConnections:
        newConnections = False
        for element, connections in elements.iteritems():
            alreadyConnectedToStart = element in elementsConnectedToStart
            connectedToStart = any(x in elementsConnectedToStart for x in connections)
            if not alreadyConnectedToStart and connectedToStart:
                elementsConnectedToStart.append(element)
                newConnections = True

    return elementsConnectedToStart

print elements

groups = 0
while len(elements.keys()) > 0:
    elementsToRemove = findGroup(elements, list(elements.keys())[0])
    for e in elementsToRemove:
        elements.pop(e)
    groups += 1
    
print groups
