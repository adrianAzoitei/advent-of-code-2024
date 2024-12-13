from operator import mul, add
import itertools as it

Operations = list[tuple[int, list[int]]]
def open_file(filename: str) -> Operations:
    with open(filename, "r") as input:
        ops: Operations = []
        for line in input.read().splitlines():
            ops.append((int(line.split(':')[0]), list(map(int, line.split(':')[1].strip().split(' ')))))
    return ops


def concat(left: int, right: int) -> int:
    return int(f"{left}{right}")
            

def find_valid_ops(ops: Operations, concatenate: bool = False) -> Operations:
    valid = []
    for operation in ops:
        res, numbers = operation[0], operation[1]
        if concatenate:
            candidates = list(it.product([mul, add, concat], repeat=(len(numbers) - 1)))
        else:
            candidates = list(it.product([mul, add], repeat=(len(numbers) - 1)))
        for candidate in candidates:
            running_res = 0
            for i, n in enumerate(numbers):
                if i == 0:
                    running_res = n
                else:
                    running_res = candidate[i-1](running_res, n)
                if running_res > res:
                    break
            if running_res == res:
                valid.append(operation)
                break
    return valid


def sum_valid_ops(ops: Operations) -> int:
    return sum([op[0] for op in ops])


def test_sum_valid_ops_example():
    assert sum_valid_ops(find_valid_ops(open_file("day-7-example"))) == 3749


def test_sum_valid_ops_example_with_concatenation():
    assert sum_valid_ops(find_valid_ops(open_file("day-7-example"), True)) == 14043


if __name__ == "__main__":
    print(f"part 1: {sum_valid_ops(find_valid_ops(open_file('day-7-input')))}")
    print(f"part 1: {sum_valid_ops(find_valid_ops(open_file("day-7-input"), True))}")
