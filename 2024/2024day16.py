import heapq
p = open('AdventOfCode/Advent of Code Inputs/2024day16TEST2.txt').read().split('\n')
puzzle = []

for i in p:
    puzzle.append([j for j in i])

def partOne():
    maze = puzzle.copy()
    
    def djikstra(graph, start, end):
        distances = {}
        for x in range(len(graph)):
            for y in range(len(graph[0])):
                distances[(x, y)] = float('inf')
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            currDist, currNode = heapq.heappop(pq)
            if currDist > distances[currNode]:
                continue
            
            if graph[currNode[0]][currNode[1]] == '#':
                continue

            if graph[currNode[0]][currNode[1]] == '.':
                continue

            for neighbor, weight in graph[currNode[0]].items():
                distance = currDist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances

    start = (0, 0)
    end = (0, 0)
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 'S':
                start = (x, y)
            if maze[x][y] == 'E':
                end = (x, y)
    ans = djikstra(maze, start, end)
    
    print(f'Part One: {ans}')

def partTwo():
    pass

partOne()
partTwo()