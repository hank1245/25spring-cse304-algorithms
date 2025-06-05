import sys
import importlib.util
from random import sample

module_name = "selection.sort"
file_path = "7.2.selection.sort.py"

test_cases = []
for i in range(10):
    S = sample(range(1, 100), 10*i)
    test = {"input": S, "expected": sorted(S), "desc": ""}
    test_cases.append(test)

def run_test_cases(file_path="7.2.selection.sort.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    sort_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sort_module)

    # selection sort function is named `selectionsort(n, S)`
    sort_func = sort_module.selectionsort
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        arr = case["input"].copy()  # copy so the original isn't modified
        expected = case["expected"]

        # call selectionsort with length and list
        sort_func(len(arr), arr)

        if arr == expected:
            passed += 1
            print(f"✅Test {i} 통과: {case['desc']} \n-> Expected: {expected}, Got: {arr}\n")
        else:
            print(f"❌Test {i} 실패: {case['desc']} \n-> Expected: {expected}, Got: {arr}\n")

    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()