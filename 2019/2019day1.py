p = open('AdventOfCode/Advent of Code Inputs/2019day1.txt').read().split('\n')

def partOne():
    ans = 0

    def calc(line):
        return (int(line) // 3) - 2
    
    for i in p:
        ans += calc(i)
    print(f"Part One: {ans}")

def partTwo():
    ans = 0
    fuels = []

    def calc(line):
        fuels.append((int(line) // 3) - 2)
        return (int(line) // 3) - 2
    
    def fuelCalc(fuel, res=0):
        fuel = (fuel // 3) - 2
        if fuel > 0:
            res += fuel
            return fuelCalc(fuel, res)
        else:
            return res

    for i in p:
        ans += calc(i)
    
    for i in fuels:
        ans += fuelCalc(i)
    print(f"Part Two: {ans}")

partOne()
partTwo()