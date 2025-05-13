from typing import List

def promising(i: int, n: int, col: List[int]) -> bool:
    is_promising = True
    k = 1
    while k < i and is_promising:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            is_promising = False
        k += 1
    return is_promising

def nqueens(i: int, n: int, col: List[int]) -> None:
    if promising(i, n, col):
        if i == n:
            print(f"found={col[1:]}")
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                nqueens(i + 1, n, col)
