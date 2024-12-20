import itertools as it
import numpy as np
from cmath import phase
from math import pi, isclose

np.set_printoptions(
    threshold=np.inf, linewidth=np.inf
)  # turn off summarization, line-wrapping


def open_file(filename: str) -> list[list[str]]:
    with open(filename, "r") as input:
        grid = [list(line.rstrip()) for line in input.readlines()]
    return grid


def find_antennas(grid: list[list[str]]) -> dict:
    parsed = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            char = grid[row][col]
            coord = complex(row, col)
            if char != ".":
                if char not in parsed.keys():
                    parsed[char] = [coord]
                else:
                    parsed[char].append(coord)
    return parsed


def grid_to_coord(grid: list[list[str]]) -> dict:
    parsed = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            char = grid[row][col]
            coord = complex(row, col)
            parsed[coord] = char
    return parsed


def find_antinodes(filename: str) -> int:
    anodes = set()
    grid = open_file(filename)
    antennas = find_antennas(grid)
    for _, coords in antennas.items():
        pairs = list(it.combinations(coords, 2))
        for left, right in pairs:
            slope = left - right
            anode_1 = left + slope
            anode_2 = right - slope
            if 0 <= anode_1.real < len(grid) and 0 <= anode_1.imag < len(grid[0]):
                anodes.add(anode_1)
            if 0 <= anode_2.real < len(grid) and 0 <= anode_2.imag < len(grid[0]):
                anodes.add(anode_2)
    return len(anodes)


def phases_equal(phases: list[float]) -> bool:
    for i, ph in enumerate(phases):
        others = phases.copy()
        others.pop(i)
        if isclose(ph, others[0]) and isclose(ph, others[1]):
            return True
        mirror = pi - ph
        if isclose(mirror, others[0]) and isclose(mirror, others[1]):
            return True
    return False


def find_collinear_antinodes(filename: str, print: bool = False) -> int:
    anodes = set()
    grid = open_file(filename)
    antennas = find_antennas(grid)
    grid_coords = grid_to_coord(grid)
    for _, coords in antennas.items():
        pairs = list(it.combinations(coords, 2))
        for left, right in pairs:
            anodes.add(left)
            anodes.add(right)
            for grid_point, _ in grid_coords.items():
                if left == grid_point or right == grid_point:
                    continue
                vectors = list(it.combinations([left, right, grid_point], 2))
                phases = list(map(lambda v: abs(phase(v[1] - v[0])), vectors))
                if phases_equal(phases):
                    anodes.add(grid_point)
    if print:
        print_grid(grid, anodes)
    return len(anodes)


def print_grid(grid: list[list[str]], anodes: set[complex], keyword: str = ""):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            candidate = complex(row, col)
            if candidate in anodes:
                char = grid[row][col]
                if char != ".":
                    grid[row][col] = "H"
                else:
                    grid[row][col] = "#"
    matrix = np.array(grid)
    with open(f"day-8-output-{keyword}", "w") as f:
        f.write(
            np.array2string(matrix, separator="", formatter={"all": lambda x: x})
            .replace("[", "")
            .replace("]", "")
        )


def test_find_antinodes():
    assert find_antinodes("./day-8-example") == 14


def test_find_antinodes_collinear():
    assert find_collinear_antinodes("./day-8-example") == 34


if __name__ == "__main__":
    print(f"part 1: {find_antinodes("./day-8-input")}")
    print(f"part 2: {find_collinear_antinodes("./day-8-input", True)}")
