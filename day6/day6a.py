def indexOfBankWithMostBlocks(banks):
    index = 0
    while max(banks) != banks[index]:
        index = index + 1
    return index;

banks = map(int, open("input").read().split())
archive = []
archive.append(list(banks))

print banks

iteration = 0
while archive.count(banks) <= 1:
    # find biggest bank
    i = indexOfBankWithMostBlocks(banks)

    # blocks to redis
    redisBlocks = banks[i]

    # zero the index value
    banks[i] = 0

    # redistribute
    while (redisBlocks > 0):
        i = (i + 1) % len(banks)
        redisBlocks = redisBlocks - 1
        banks[i] = banks[i] + 1

    #add to archive
    archive.append(list(banks))
    iteration = iteration + 1
    print banks

print iteration
