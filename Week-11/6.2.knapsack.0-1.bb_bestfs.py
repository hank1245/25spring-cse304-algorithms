from heapq import heappush, heappop
from typing import List

class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = 0

def boundof(u: Node, n: int, W: float, w: List[float], p: List[float]) -> float:
    if u.weight >= W:
        return 0
    else:
        # Complete the code here

def knapsack3(n: int, W: float, w: List[float], p: List[float]) -> float:
    global count
    heap = [] # Initialize Priority Queue
    v = Node(0, 0, 0)
    v.bound = boundof(v, n, W, w, p)
    maxprofit = 0
    heappush(heap, (-v.bound, v))
    count +=1
    while len(heap) != 0:
        # Complete the code here

    return maxprofit
