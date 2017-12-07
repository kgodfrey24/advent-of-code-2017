

programme = map(int, open("input").read().splitlines())

pc = 0
steps = 0
while pc >= 0 and pc < len(programme):
    newPc = pc + programme[pc]
    programme[pc] = programme[pc] + 1
    pc = newPc
    steps = steps + 1

print steps
