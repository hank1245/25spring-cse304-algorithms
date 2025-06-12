from typing import List

class Heap:
    def __init__(self, n: int, S: List[int]) -> None:
        self.size = n
        self.H = S

def siftdown(H: Heap, i: int) -> None:
    siftkey = H.H[i]
    parent = i
    spotfound = False
    
    while 2 * parent <= H.size and not spotfound:
        if 2 * parent < H.size and H.H[2 * parent] < H.H[2 * parent + 1]:
            largerchild = 2 * parent + 1
        else:
            largerchild = 2 * parent
        
        if siftkey < H.H[largerchild]:
            H.H[parent] = H.H[largerchild]
            parent = largerchild
        else:
            spotfound = True
    
    H.H[parent] = siftkey

def root(H: Heap) -> int:
    keyout = H.H[1]
    H.H[1] = H.H[H.size]
    H.size -= 1
    if H.size > 0:
        siftdown(H, 1)
    return keyout

def removekeys(n: int, H: Heap, S: List[int]) -> None:
    for i in range(n, 0, -1):
        S[i] = root(H)

def makeheap(n: int, H: Heap) -> None:
    for i in range(n // 2, 0, -1):
        siftdown(H, i)

def heapsort(n: int, H: Heap, S: List[int]) -> None:
    makeheap(n, H)
    removekeys(n, H, S)
