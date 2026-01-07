# Fuel Counter-Upper

def fuelCounterUpper(p):
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
    print(f'Part One: {ans}')
    
    for i in fuels:
        ans += fuelCalc(i)
    print(f"Part Two: {ans}")

    return ans

if __name__ == '__main__':
    fuelCounterUpper(open('Advent of Code Inputs/2019day1.txt').read().split('\n'))