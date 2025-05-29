import importlib.util

module_name = "knapsack2_algo"

# Updated test cases for knapsack2: each with n, W, w[], p[], expected max profit, and description
test_cases = [
    {"n": 0, "W": 100.0, "w": [],                    "p": [],               "expected": 0.0,  "desc": "no items"},
    {"n": 1, "W": 0.0,   "w": [10],                  "p": [100],            "expected": 0.0,  "desc": "zero capacity single"},
    {"n": 3, "W": 5.0,   "w": [2, 3, 4],             "p": [3, 4, 5],        "expected": 7.0,  "desc": "combination yields max profit 7"},
    {"n": 3, "W": 50.0,  "w": [60, 70, 80],         "p": [10, 20, 30],      "expected": 0.0,  "desc": "all items too heavy"},
    {"n": 4, "W": 10.0,  "w": [5, 4, 6, 3],         "p": [10, 40, 30, 50], "expected": 90.0, "desc": "optimal is item 2 + 4"},
    {"n": 5, "W": 11.0,  "w": [1, 2, 5, 6, 7],      "p": [1, 6, 18, 22, 28],"expected": 40.0, "desc": "textbook example"},
    {"n": 3, "W": 100.0, "w": [20, 30, 40],         "p": [40, 50, 60],      "expected": 150.0,"desc": "all fit sum profits"},
    {"n": 6, "W": 15.0,  "w": [1, 2, 3, 8, 7, 4],   "p": [1, 2, 5, 10, 8, 4],"expected": 19.0, "desc": "optimal is items 3 + 4 + 6"},
    {"n": 5, "W": 7.0,   "w": [3, 2, 4, 1, 5],      "p": [4, 3, 5, 3, 6],    "expected": 11.0, "desc": "mixed small items"},
    {"n": 4, "W": 8.0,   "w": [4, 5, 3, 2],         "p": [6, 10, 5, 3],      "expected": 15.0, "desc": "optimal is item 2 + 3"},
]

def run_test_cases(file_path="6.1.knapsack.0-1.bb_bfs.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    ks_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ks_module)

    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        print(f"\n\033[1mExample {i}: {case['desc']}\033[0m")

        n = case["n"]
        W = case["W"]
        w = [0] + case["w"]
        p = [0] + case["p"]
        # Pad lists for empty cases
        if len(w) <= 1:
            w.append(0)
            p.append(0)
        result = ks_module.knapsack2(n, W, w, p)
        expected = case["expected"]
        print(f"Max profit: {result}")

        if abs(result - expected) < 1e-6:
            print("출력: ✅ Passed")
            passed += 1
        else:
            print(f"출력: ❌ Failed (Expected: {expected}, Got: {result})")

        print("-" * 40)

    print(f"\n✅ {passed}/{total} 테스트 케이스 통과")

if __name__ == '__main__':
    run_test_cases()
