from typing import List

def partition(low: int, high: int, S: List[int]) -> int:
    pivotitem = S[low]
    j = low
    
    for i in range(low + 1, high + 1):
        if S[i] < pivotitem:
            j += 1
            S[i], S[j] = S[j], S[i]
    
    S[low], S[j] = S[j], S[low]
    return j

def quicksort(low: int, high: int, S: List[int]) -> None:
    if low < high:
        pivotpoint = partition(low, high, S)
        quicksort(low, pivotpoint - 1, S)
        quicksort(pivotpoint + 1, high, S)