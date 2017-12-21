input = open("input").read()

print input

shouldIgnoreNextChar = False
garbageMode = False
groupNestedLevel = 0
count = 0

for c in input:
    if shouldIgnoreNextChar:
        shouldIgnoreNextChar = False
    elif c == "!":
        shouldIgnoreNextChar = True
    elif c == "<" and not garbageMode:
        garbageMode = True
    elif c == ">":
        garbageMode = False
    elif garbageMode:
        count = count + 1

print count
