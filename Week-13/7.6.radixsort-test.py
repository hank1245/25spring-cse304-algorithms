import sys
import importlib.util
from random import sample

module_name = "radixsort_module"
file_path = "7.6.radixsort.py"

test_cases = []
for size in range(0, 100, 10):
    lst = sample(range(0, 1000), size)
    test_cases.append({
        "input": lst,
        "expected": sorted(lst),
        "desc": f"length={size}"
    })

def run_test_cases(file_path="7.6.radixsort.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    from_list = mod.from_list
    to_list   = mod.to_list
    radixsort = mod.radixsort

    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        orig = case["input"]
        expected = case["expected"]

        head = from_list(orig)

        max_key = max(orig) if orig else 0
        num_digits = len(str(max_key))

        sorted_head = radixsort(head, num_digits)
        result = to_list(sorted_head)

        if result == expected:
            passed += 1
            print(f"✅ Test {i} 통과: {case['desc']}")
        else:
            print(f"❌ Test {i} 실패: {case['desc']}")
            print(f"   Expected: {expected}")
            print(f"   Got     : {result}")

    print(f"\n✅ {passed}/{total} 테스트 케이스 통과")

if __name__ == "__main__":
    run_test_cases()
