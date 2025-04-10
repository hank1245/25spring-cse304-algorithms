import time

def bin(n: int, k: int) -> int:
    if k == 0 or n == k:
        return 1
    else:
        # Complete the code here
        # binomial coefficient divide and conquer
        return bin(n - 1, k - 1) + bin(n - 1, k)