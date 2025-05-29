from heapq import heappush, heappop
from typing import List, Tuple
import time

INF = float("inf")

class Node:
    def __init__(self, level, path):
        self.level = level
        self.path = path[:]
        self.bound = 0

def remainder(path: List[int], n: int) -> int:
    return n * (n + 1) // 2 - sum(path)

def pathlength(path: List[int], W: List[List[float]]) -> float:
    # Complete the code here

    return length

def hasOutgoing(v: int, path: List[int]) -> bool:
    return v in path[:len(path)-1]

def hasIncoming(v: int, path: List[int]) -> bool:
    return v in path[1:]

def boundof(v: Node, n: int, W: List[List[float]]) -> float:
    global INF
    lower = pathlength(v.path, W)
    for i in range(1, n + 1):
        # Complete the code here

    return lower

def travel2(n: int, W: List[List[float]]) -> Tuple[float, List[int]]:
    global INF
    heap = [] # Initialize Priority Queue
    v = Node(0, [1])
    v.bound = boundof(v, n, W)
    minlength, opttour = INF, []
    heappush(heap, (v.bound, time.time(), v))
    while len(heap) != 0:
        v = heappop(heap)[2]
        if v.bound < minlength:
            for i in range(2, n + 1):
                # Complete the code here
                
    return minlength, opttour
