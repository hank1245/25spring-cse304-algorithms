from typing import List

def insertionsort(n: int, S: List[int]) -> None:
    for i in range(1, n):
        x = S[i]
        j = i - 1
        while j >= 0 and S[j] > x:
            S[j + 1] = S[j]
            j -= 1
        S[j + 1] = x