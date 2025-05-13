from typing import Dict, Tuple

def knapsack(n: int, W: int, DP: Dict[Tuple[int, int], int]) -> int:
    global w, p
    
    if n == 0 or W <= 0:
        return 0

    if (n, W) in DP:
        return DP[(n, W)]

    if w[n] > W:
        result = knapsack(n - 1, W, DP)
    else:
        include_profit = p[n] + knapsack(n - 1, W - w[n], DP)
        exclude_profit = knapsack(n - 1, W, DP)
        result = max(include_profit, exclude_profit)
        
    DP[(n, W)] = result
    return result