from heapq import heappush, heappop
from typing import List, Tuple
import time

INF = float("inf")

class Node:
    def __init__(self, level, path):
        self.level = level
        self.path = path[:]
        self.bound = 0

def pathlength(path: List[int], W: List[List[float]]) -> float:
    length = 0
    for i in range(1, len(path)):
        cost = W[path[i-1]][path[i]]
        if cost == INF:
            return INF
        length += cost
    return length

def hasOutgoing(i: int, path: List[int]) -> bool:
    return i in path[:-1]

def hasIncoming(j: int, path: List[int]) -> bool:
    return j in path[1:]

def boundof(v: Node, n: int, W: List[List[float]]) -> float:
    lower = pathlength(v.path, W)
    for i in range(1, n+1):
        if hasOutgoing(i, v.path):
            continue
        minimum = INF
        for j in range(1, n+1):
            if i == j:
                continue
            if j == 1 and i == v.path[-1]:
                continue
            if hasIncoming(j, v.path):
                continue
            if W[i][j] < minimum:
                minimum = W[i][j]
        lower += minimum
    return lower

def travel2(n: int, W: List[List[float]]) -> Tuple[float, List[int]]:
    heap = []
    v = Node(0, [1])
    v.bound = boundof(v, n, W)
    minlength = INF
    opttour = []
    heappush(heap, (v.bound, time.time(), v))
    while heap:
        v = heappop(heap)[2]
        if v.bound < minlength:
            u_level = v.level + 1
            for i in range(2, n+1):
                if i not in v.path:
                    u_path = v.path + [i]
                    if u_level == n-2:
                        left = [j for j in range(2, n+1) if j not in u_path]
                        assert len(left) == 1
                        u_path2 = u_path + [left[0], 1]
                        cost = pathlength(u_path2, W)
                        if cost < minlength:
                            minlength = cost
                            opttour = u_path2
                    else:
                        u = Node(u_level, u_path)
                        u.bound = boundof(u, n, W)
                        if u.bound < minlength:
                            heappush(heap, (u.bound, time.time(), u))
    return minlength, opttour
