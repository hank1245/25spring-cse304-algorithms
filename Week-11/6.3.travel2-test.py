import importlib.util
import time
from itertools import count

INF = float('inf')
_timer = count()
time.time = lambda: next(_timer)

module_name = "travel2_algo"

test_cases = [
    # 1. Triangle (3 nodes)
    {
        "n": 3,
        "W": [
            [INF, INF, INF, INF],
            [INF, 0, 10, 15],
            [INF, 10, 0, 20],
            [INF, 15, 20, 0]
        ],
        "expected": 45.0,
        "desc": "simple triangle"
    },
    # 2. Square (4 nodes) 
    {
        "n": 4,
        "W": [
            [INF, INF, INF, INF, INF],
            [INF, 0, 5, 9, 8],
            [INF, 5, 0, 7, 6],
            [INF, 9, 7, 0, 4],
            [INF, 8, 6, 4, 0]
        ],
        "expected": 5+7+4+8,  # best tour 1-2-3-4-1
        "desc": "square symmetric"
    },
        # 3. Asymmetric 4 nodes 
    {
        "n": 4,
        "W": [
            [INF, INF, INF, INF, INF],
            [INF, 0, 3, 4, 2],
            [INF, 2, 0, 6, 3],
            [INF, 7, 5, 0, 4],
            [INF, 3, 6, 2, 0]
        ],
        "expected": 11.0,  # algorithm returns 11 via tour [1,4,3,2,1]
        "desc": "asymmetric"
    },
        # 4. 5 nodes simple 
    {
        "n": 5,
        "W": [
            [INF]*6,
            [INF,0,2,9,10,7],
            [INF,1,0,6,4,3],
            [INF,15,7,0,8,5],
            [INF,6,3,12,0,4],
            [INF,10,4,8,9,0]
        ],
        "expected": 26.0,  # algorithm returns 26 via tour [1,3,4,5,2,1]
        "desc": "5-node mix"
    },
        # 5. Line graph 4 nodes 
    {
        "n":4,
        "W":[
            [INF]*5,
            [INF,0,1,INF,INF],
            [INF,1,0,1,INF],
            [INF,INF,1,0,1],
            [INF,INF,INF,1,0]
        ],
        "expected": float('inf'),  # no Hamiltonian cycle
        "desc": "line graph no tour"
    },
        # 6. Star graph 5 nodes 
    {
        "n":5,
        "W":[
            [INF]*6,
            [INF,0,1,1,1,1],
            [INF,1,0,INF,INF,INF],
            [INF,1,INF,0,INF,INF],
            [INF,1,INF,INF,0,INF],
            [INF,1,INF,INF,INF,0]
        ],
        "expected": float('inf'),
        "desc": "star center no cycle"
    },
        # 7. 3 nodes equal weights 
    {
        "n":3,
        "W":[
            [INF]*4,
            [INF,0,5,5],
            [INF,5,0,5],
            [INF,5,5,0]
        ],
        "expected": 5+5+5,
        "desc": "equilateral triangle"
    },
        # 8. 4 nodes with zero edges 
    {
        "n":4,
        "W":[
            [INF]*5,
            [INF,0,0,0,0],
            [INF,0,0,0,0],
            [INF,0,0,0,0],
            [INF,0,0,0,0]
        ],
        "expected": 0,
        "desc": "zero-cost full graph"
    },
        # 9. Small random 5 nodes 
    {
        "n":5,
        "W":[
            [INF]*6,
            [INF,0,3,8,5,9],
            [INF,3,0,7,6,4],
            [INF,8,7,0,4,3],
            [INF,5,6,4,0,2],
            [INF,9,4,3,2,0]
        ],
        "expected": 19.0,  # algorithm returns 19 via tour [1,2,5,3,4,1] 
        "desc": "random small" 
    },
        # 10. 6 nodes simple cycle 
    {
        "n":6,
        "W":[
            [INF]*7,
            [INF,0,1,INF,INF,INF,1],
            [INF,1,0,1,INF,INF,INF],
            [INF,INF,1,0,1,INF,INF],
            [INF,INF,INF,1,0,1,INF],
            [INF,INF,INF,INF,1,0,1],
            [INF,1,INF,INF,INF,1,0]
        ],
        "expected": 6,
        "desc": "6-cycle graph"
    }
]

def run_test_cases(file_path="6.3.travel2.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    ts_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ts_module)

    passed, total = 0, len(test_cases)
    for i, case in enumerate(test_cases, 1):
        n, W, expected, desc = case["n"], case["W"], case["expected"], case["desc"]
        print(f"\n\033[1mExample {i}: {desc}\033[0m")
        try:
            minlength, opttour = ts_module.travel2(n, W)
        except TypeError as e:
            print(f"❌ Error for {desc}: {e}")
            continue
        print(f"minlength: {minlength}, opttour: {opttour}")
        if expected == float('inf'):
            if minlength == float('inf'):
                print("✅ Passed")
                passed += 1
            else:
                print(f"❌ Failed (Expected: INF, Got: {minlength})")
        else:
            if abs(minlength - expected) < 1e-6:
                print("✅ Passed")
                passed += 1
            else:
                print(f"❌ Failed (Expected: {expected}, Got: {minlength})")
    print(f"\n✅ {passed}/{total} test cases passed")


if __name__ == '__main__':
    run_test_cases()
