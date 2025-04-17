from typing import List, Tuple

def dijkstra(n: int, W: List[List[float]]) -> List[Tuple[int, int, float]]:
    F = []
    INF = float("inf")
    touch = [-1] * (n + 1)
    length = [-1] * (n + 1)

    for i in range(2, n + 1):
        touch[i] = 1
        length[i] = W[1][i]

    for _ in range(n - 1):
        min_len = INF
        vnear = -1
        for i in range(2, n + 1):
            if 0 <= length[i] < min_len:
                min_len = length[i]
                vnear = i

        if vnear == -1:
            break

        edge = (touch[vnear], vnear, W[touch[vnear]][vnear])
        F.append(edge)

        for i in range(2, n + 1):
            if W[vnear][i] != INF and length[vnear] + W[vnear][i] < length[i]:
                length[i] = length[vnear] + W[vnear][i]
                touch[i] = vnear

        length[vnear] = -1
    return F