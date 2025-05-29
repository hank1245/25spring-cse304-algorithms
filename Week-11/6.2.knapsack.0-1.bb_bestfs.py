from heapq import heappush, heappop
from typing import List

count = 0

class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = 0

    def __lt__(self, other):
        return self.bound > other.bound 

def boundof(u: Node, n: int, W: float, w: List[float], p: List[float]) -> float:
    if u.weight > W:
        return 0
    bound = u.profit
    j = u.level + 1
    totweight = u.weight
    while j <= n and totweight + w[j] <= W:
        totweight += w[j]
        bound += p[j]
        j += 1
    if j <= n:
        bound += (W - totweight) * p[j] / w[j]
    return bound

def knapsack3(n: int, W: float, w: List[float], p: List[float]) -> float:
    global count
    count = 0
    heap = []
    v = Node(0, 0, 0)
    v.bound = boundof(v, n, W, w, p)
    maxprofit = 0.0
    counter = 0
    heappush(heap, (-v.bound, counter, v))
    count += 1
    counter += 1
    while heap:
        _, _, v = heappop(heap)
        if v.bound > maxprofit and v.level < n:
            u = Node(v.level + 1, v.weight + w[v.level + 1], v.profit + p[v.level + 1])
            if u.weight <= W and u.profit > maxprofit:
                maxprofit = u.profit
            u.bound = boundof(u, n, W, w, p)
            if u.bound > maxprofit:
                heappush(heap, (-u.bound, counter, u))
                count += 1
                counter += 1
            u = Node(v.level + 1, v.weight, v.profit)
            u.bound = boundof(u, n, W, w, p)
            if u.bound > maxprofit:
                heappush(heap, (-u.bound, counter, u))
                count += 1
                counter += 1
    return maxprofit
