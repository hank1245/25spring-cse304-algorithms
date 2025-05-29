from typing import List

# Initialize global count variable
count = 0

class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit

def boundof(u: Node, n: int, W: float, w: List[float], p: List[float]) -> float:
    if u.weight >= W:
        return 0
    else:
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

def knapsack2(n: int, W: float, w: List[float], p: List[float]) -> float:
    global count
    count = 0  
    queue = []
    v = Node(0, 0, 0)
    bound = boundof(v, n, W, w, p)
    maxprofit = 0
    queue.append(v)
    count += 1
    while len(queue) != 0:
        v = queue.pop(0) 
        
        if v.level == n:  
            continue
            
        u = Node(v.level + 1, v.weight + w[v.level + 1], v.profit + p[v.level + 1])
        
        if u.weight <= W and u.profit > maxprofit:
            maxprofit = u.profit
            
        u.bound = boundof(u, n, W, w, p)
        if u.bound > maxprofit:
            queue.append(u)
            count += 1
            
        u = Node(v.level + 1, v.weight, v.profit)
        u.bound = boundof(u, n, W, w, p)
        if u.bound > maxprofit:
            queue.append(u)
            count += 1
        
    return maxprofit
