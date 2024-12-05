from functools import cmp_to_key

Rule = tuple[int, int] 
Update = list[int] 

def open_file(filename: str) -> tuple[dict[Rule, int], list[Update]]:
    rules = {}
    updates = []
    with open(filename, "r") as input:
        for line in input.readlines():
            if '|' in line:
                rule = tuple(map(int, line.split('|')))
                rules[(rule[0]), rule[1]] = 1
                rules[(rule[1]), rule[0]] = -1
            if ',' in line:
                update = list(map(int, line.split(',')))
                updates.append(update)
    return rules, updates


def is_order_correct(update: Update, rules: dict[Rule, int]) -> bool:
    for slow in range(len(update)):
        for fast in range(slow + 1, len(update)):
            rule = (update[slow], update[fast])
            if rule in rules and rules[rule] == -1:
                return False
    return True


def find_correctly_ordered_updates(filename: str) -> list[Update]:
    rules, updates = open_file(filename)
    correct = []

    for update in updates:
        if is_order_correct(update, rules):
            correct.append(update)

    return correct



def fix_updates(filename: str) -> list[Update]:
    rules, updates = open_file(filename)
    fixed = []

    def cmp(x, y):
        correct = rules.get((x, y), 0)
        return correct

    for i, update in enumerate(updates):
        if is_order_correct(update, rules): continue
        update.sort(key=cmp_to_key(cmp), reverse=True) 
        fixed.append(update)

    return fixed


def sum_middle_page_numbers(updates: list[Update]) -> int:
    return sum(update[len(update) // 2] for update in updates)


def sum_middle_from_correct_updates(filename: str) -> int:
    return sum_middle_page_numbers(find_correctly_ordered_updates(filename))


def sum_middle_from_fixed_updates(filename: str) -> int:
    return sum_middle_page_numbers(fix_updates(filename))


def test_sum_middle_from_correct_updates_example():
    assert sum_middle_from_correct_updates("day-5-example") == 143



def test_sum_middle_from_all_updates_example():
    assert sum_middle_from_fixed_updates("day-5-example") == 123


if __name__ == "__main__":
    print(f"part 1: {sum_middle_from_correct_updates("day-5-input")}")
    print(f"part 2: {sum_middle_from_fixed_updates("day-5-input")}")

