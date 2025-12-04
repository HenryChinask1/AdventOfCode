def partOne():
    batteryRows = open('Advent of Code Inputs/2025day3.txt').read().split('\n')
    res = 0

    def checkBattery(battery):    
        ans = 0
        idx = 0
        battery = list(int(i) for i in battery)

        for i in range(len(battery) - 1):
            if battery[i] == 9:
                return [90, i]
            if battery[i] > ans:
                ans = battery[i]
                idx = i
        return [ans * 10, idx]
        
    for row in batteryRows:
        checked = checkBattery(row)
        tempAns = 0
        row = list(int(i) for i in row[checked[1] + 1:])
        for i in row:
            if i > tempAns:
                tempAns = i
        res += checked[0] + tempAns
        
    print(f'Part One: {res}')


def partTwo():
    batteryRows = open('Advent of Code Inputs/2025day3TEST.txt').read().split('\n')
    res = 0

    def checkBattery(battery):    
        ans = 0
        idx = 0
        battery = list(int(i) for i in battery)

        for i in range(len(battery) - 1):
            if battery[i] == 9:
                return [90, i]
            if battery[i] > ans:
                ans = battery[i]
                idx = i
        return [ans * 10, idx]
        
    for row in batteryRows:
        checked = checkBattery(row)
        tempAns = 0
        row = list(int(i) for i in row[checked[1] + 1:])
        for i in row:
            if i > tempAns:
                tempAns = i
        res += checked[0] + tempAns
        
    print(f'Part Two: {res}')

partOne()
partTwo()