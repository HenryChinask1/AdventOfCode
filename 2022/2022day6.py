data = open('Advent of Code Inputs/2022day6.txt').read()
dataBuffer = [x for x in data]


# Part 1 - Packet Markers.
for i in range(len(dataBuffer) - 4 + 1):
    if len(set(dataBuffer[i: i + 4])) == 4:
        print(f'Part One: {i+4}')
        break

# Part 2 - Message Markers.
for i in range(len(dataBuffer) - 14 + 1):
    if len(set(dataBuffer[i: i + 14])) == 14:
        print(f'Part Two: {i + 14}')
        break