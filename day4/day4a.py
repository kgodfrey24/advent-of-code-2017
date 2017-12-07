with open("input") as f:
    content = f.readlines()

validLines = 0
for row in content:
    wordList = row.split()
    wordSet = set(wordList)
    if len(wordSet) == len(wordList):
        validLines = validLines + 1


print validLines
