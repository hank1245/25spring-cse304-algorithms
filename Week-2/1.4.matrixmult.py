# name: 김희웅
# student id: 2019101485
from typing import List

def matrixmult(n: int, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    C = [[0] * n for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            C[i][j] = 0
            for k in range(0,n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]

    return C