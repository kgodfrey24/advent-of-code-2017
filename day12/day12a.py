mappings = map(str.split, open("input").read().translate(None, ',<->').splitlines())

elements = {}
for m in mappings:
    elements[m[0]] = m[1:]

elementsConnectedToZero = ["0"]
newConnections = True
while newConnections:
    newConnections = False
    for element, connections in elements.iteritems():
        alreadyConnectedToZero = element in elementsConnectedToZero
        connectedToZero = any(x in elementsConnectedToZero for x in connections)
        if not alreadyConnectedToZero and connectedToZero:
            elementsConnectedToZero.append(element)
            newConnections = True

print elementsConnectedToZero
print len(elementsConnectedToZero)
