input = open("input").read()

print input

shouldIgnoreNextChar = False
garbageMode = False
groupNestedLevel = 0
score = 0

for c in input:
    if shouldIgnoreNextChar:
        shouldIgnoreNextChar = False
    elif c == "!":
        shouldIgnoreNextChar = True
    elif c == "{" and not garbageMode:
        groupNestedLevel = groupNestedLevel + 1
    elif c == "}" and not garbageMode:
        score = score + groupNestedLevel
        groupNestedLevel = groupNestedLevel - 1
    elif c == "<":
        garbageMode = True
    elif c == ">":
        garbageMode = False

print score
