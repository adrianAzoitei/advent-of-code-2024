
# examples
LEFT_LIST = [3, 4, 2, 1, 3, 3]
RIGHT_LIST = [4, 3, 5, 3, 9, 3]

def total_distance_between_lists(left: list[int], right: list[int]) -> int:
   return sum([abs(l - r) for l, r in zip(sorted(left), sorted(right))])

def test_total_distance_between_lists():
    assert total_distance_between_lists(LEFT_LIST, RIGHT_LIST) == 11


def find_list_similarity(left: list[int], right: list[int]) -> int:
    similarity_scores = {}
    total_similarity = 0

    def update_similarity_scores(i: int, right: list[int]):
        if i not in similarity_scores.keys():
            print(i)
            similarity_scores[i] = 0
            right_occurences = 0
            for j in right:
                if i == j:
                    right_occurences += 1
            similarity_scores[i] = i * right_occurences

    for i in left:
        update_similarity_scores(i, right)
        total_similarity += similarity_scores[i]

    return total_similarity

def test_find_list_similarity():
    assert find_list_similarity(LEFT_LIST, RIGHT_LIST) == 31

with open("day-1-input", "r") as input:
    left = []
    right = []
    for line in input:
        pair = line.split()
        left.append(int(pair[0]))
        right.append(int(pair[1]))

    print(total_distance_between_lists(left, right))
    print(find_list_similarity(left, right))
