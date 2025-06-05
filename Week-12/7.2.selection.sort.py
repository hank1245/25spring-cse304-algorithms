from typing import List

def selectionsort(n: int, S: List[int]) -> None:
    for i in range(n-1):
        smallest = i
        for j in range(i + 1, n):
            if S[j] < S[smallest]:
                smallest = j
        S[i], S[smallest] = S[smallest], S[i]