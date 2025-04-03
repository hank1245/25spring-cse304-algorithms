# name: 김희웅
# student id: 2019101485
def fib1(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)