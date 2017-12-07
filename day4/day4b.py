def sortWord(s):
    return ''.join(sorted(s))

with open("input") as f:
    content = f.readlines()

validLines = 0
for row in content:
    wordList = row.split()
    sortedWordList = map(sortWord, wordList)
    print sortedWordList
    wordSet = set(sortedWordList)
    if len(wordSet) == len(sortedWordList):
        validLines = validLines + 1


print validLines
