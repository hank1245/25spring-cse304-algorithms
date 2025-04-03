from typing import List

def exchangesort(n: int, S: List[int]) -> None:
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if S[i] > S[j]:
                S[i], S[j] = S[j], S[i]