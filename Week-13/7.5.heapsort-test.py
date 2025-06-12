import sys
import importlib.util
from random import sample

module_name = "heapsort"
file_path = "7.5.heapsort.py"

test_cases = []
for size in range(0, 100, 10):
    arr = sample(range(1, 100), size)
    test_cases.append({
        "input": arr,
        "expected": sorted(arr),
        "desc": f"length={size}"
    })

def run_test_cases(file_path="7.5.heapsort.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    sort_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sort_module)

    Heap = sort_module.Heap
    heapsort = sort_module.heapsort
    
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        orig = case["input"]
        expected = case["expected"]

        S = [None] + orig.copy()
        H = Heap(len(orig), S)
        heapsort(len(orig), H, S)
        result = S[1:] 

        if result == expected:
            passed += 1
            print(f"✅ Test {i} 통과: {case['desc']}")
        else:
            print(f"❌ Test {i} 실패: {case['desc']}")
            print(f"   Expected: {expected}")
            print(f"   Got     : {result}")

    print(f"\n✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()