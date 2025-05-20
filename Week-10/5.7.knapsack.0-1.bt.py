from typing import List

# Global variable type declarations
n: int
W: float
w: List[float]
p: List[float]
maxprofit: float
bestset: List[bool]
include: List[bool]

def promising(i: int, weight: float, profit: float) -> bool:
    global n, W, w, p, maxprofit
    
    if weight >= W:
        return False
        
    bound = profit
    j = i + 1
    totweight = weight
    
    while j <= n and totweight + w[j] <= W:
        totweight += w[j]
        bound += p[j]
        j += 1
    
    if j <= n:
        bound += (W - totweight) * (p[j] / w[j])
    
    return bound > maxprofit

def knapsack(i: int, weight: float, profit: float) -> None:
    global n, W, w, p, bestset, include, maxprofit
    
    if weight <= W and profit > maxprofit:
        maxprofit = profit
        for j in range(1, n + 1):
            bestset[j] = include[j]
    
    if promising(i, weight, profit):
        include[i + 1] = True
        knapsack(i + 1, weight + w[i + 1], profit + p[i + 1])
        
        include[i + 1] = False
        knapsack(i + 1, weight, profit)