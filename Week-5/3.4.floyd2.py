from typing import List

def floyd2(n: int, W: List[List[int]]) -> List[List[int]]:
    P = [[-1] * (n) for _ in range(n)]
    D = W
    # Complete the code here
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k
    return D, P

def path(i: int, j: int, P: list[list[int]]):
    k = P[i][j]
    if k != -1:
        path(i, k)
        print("v" + str(k), end = " ")
        path(k, j)