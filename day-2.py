from itertools import islice

# https://docs.python.org/release/2.3.5/lib/itertools-example.html
def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result    
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def is_report_safe(report: list[int], dampener: bool = False) -> int:
    def test_report(report: list[int]):
        direction: str | None = None
        for pair in window(report, 2):
            local_direction = "increasing" if pair[1] > pair[0] else "decreasing"
            diff = abs(pair[1] - pair[0])
            if not direction:
                direction = local_direction # init direction

            if direction != local_direction or diff > 3 or diff == 0:
                return 0
        return 1

    first_try = test_report(report)
    if first_try == 0 and dampener:
        for i in range(len(report)):
            if test_report(report[:i] + report[i+1:]) == 1:
                return 1
    return first_try
            

def test_is_report_safe():
    assert find_safe_reports("day-2-example") == 2

def test_is_report_safe_with_dampener():
    assert find_safe_reports("day-2-example", True) == 4


def find_safe_reports(filename: str, dampener: bool = False) -> int:
    with open(filename, "r") as input:
        reports = [list(map(int, line.split(' '))) for line in input.readlines()]
    return sum([is_report_safe(report, dampener) for report in reports])

if __name__ == "__main__":
    print(find_safe_reports("day-2-input", True))
