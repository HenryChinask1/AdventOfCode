# Universal Orbit Map
from collections import defaultdict

'''
SAMPLE: 42 Orbits

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
            /
           I

'''

class OrbitMap:

    def __init__(self, planet, parentPlanet=None):
        self.planet = planet
        self.children = []
        self.parentPlanet = parentPlanet
    
    def __repr__(self):
        return f'Node("{self.planet}, children={self.children})'
    
def buildMap(edges):
    adjList = defaultdict(list)
    allNodes = set()
    childNodes = set()

    for parent, child in edges:
        adjList[parent].append(child)
        allNodes.add(parent)
        allNodes.add(child)
        childNodes.add(child)
    
    root = (allNodes - childNodes).pop()

    def buildNode(nodeVal):
        node = OrbitMap(nodeVal)
        for childVal in adjList.get(nodeVal, []):
            node.children.append(buildNode(childVal))
        return node
    
    return buildNode(root)

    
if __name__ == '__main__':
    f = open('Advent of Code Inputs/2019day6TEST.txt').read().split('\n')
    f.sort(key=lambda x: x[1])
    print(f)
    data = []
    for i in f:
        data.append(i.split(')'))
    # x = OrbitMap(data.pop())
    # for i in data:
    #     x.addPlanets(i)
    # print(x.children)
    x = buildMap(data)
    
    def printTree(node, indent, ans):
        print(" " * indent + str(node.planet), ans)
        for child in node.children:
            ans += 1
            printTree(child, indent + 2, ans)
    
    printTree(x, indent=0, ans=0)
    