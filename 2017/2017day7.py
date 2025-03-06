from typing import Optional
from dataclasses import dataclass

p = open('AdventOfCode/Advent of Code Inputs/2017day7TEST.txt').read().split('\n')

@dataclass
class Node:
    def __init__(self, node):
        self.node = node
        self.children = []

class TreeNode:
    def __init__(self, Node):
        self.data = Node
        self.children = []

    def addChild(self, child):
        self.children.append(child)
    
    def removeChild(self, child):
        self.children.remove(child)

root = TreeNode('a')
child = TreeNode('b')
child2 = 'c'
root.addChild(child)
child.addChild(child2)

print(root.children)