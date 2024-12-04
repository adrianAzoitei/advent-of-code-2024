import re

def test_find_multiplications_example():
    assert find_and_compute_valid_multiplications("day-3-example") == 161

def test_find_multiplications_conditionals_example():
    assert find_and_compute_valid_multiplications_with_conditionals("day-3-example") == 48

def find_and_compute_valid_multiplications(filename: str) -> int:
    with open(filename, "r") as input:
        # https://stackoverflow.com/questions/50504500/deprecationwarning-invalid-escape-sequence-what-to-use-instead-of-d
        pairs = [tuple(map(int, re.findall(r'\d+', mul))) for mul in re.findall(r'mul\(\d{1,3},\d{1,3}\)', input.read())]
        return sum(map(lambda x: x[0] * x[1], pairs))

def find_and_compute_valid_multiplications_with_conditionals(filename: str) -> int:
    with open(filename, "r") as input:
        filtered = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', input.read())

    running_sum = 0 
    do = True
    for op in filtered:
        if 'mul' in op and do:
            pair = tuple(map(int, re.findall(r'\d+', op)))
            running_sum +=  pair[0] * pair[1]

        if op == "don't()":
            do = False

        if op == "do()":
            do = True

    return running_sum

if __name__ == "__main__":
    print(find_and_compute_valid_multiplications("day-3-input"))
    print(find_and_compute_valid_multiplications_with_conditionals("day-3-input"))
