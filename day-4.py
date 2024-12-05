def open_file(filename: str) -> tuple[list[list[str]], int, int]:
    with open(filename, "r") as input:
        grid = [list(line.rstrip()) for line in input.readlines()]
    return grid, len(grid[0]), len(grid)


def find_searchstring(filename: str, searchstring: str = "XMAS"):
    grid, MAX_X, MAX_Y = open_file(filename)
    
    ans = 0

    # build direction vectors
    dir_vectors = []
    for dcol in range(-1, 2):
        for drow in range(-1, 2):
            dir_vectors.append((dcol, drow))

 #           -1
 #           |        
 #           |
 #           |
 #   -1 ------------ 1 dx
 #           |        
 #           |
 #           |
 #           1 
 #           dy

    def search_in_direction(vector: tuple[int, int], coordinates: tuple[int, int], searchstring: str) -> bool:
        i = coordinates[0]
        j = coordinates[1]

        for steps, target_char in enumerate(searchstring):
            ii = i + steps * vector[1]
            jj = j + steps * vector[0]

            if not (0 <= ii < MAX_Y and 0 <= jj < MAX_X):
                return False
            
            if grid[ii][jj] != target_char:
                return False

        return True

    for i in range(MAX_Y):  # MAX_Y # loop through rows
        for j in range(MAX_X): # loop through each column in row
            for vector in dir_vectors:
                if search_in_direction(vector, (i, j), searchstring):
                    ans +=1 

    return ans


def test_find_xmas_example():
    assert find_searchstring("day-4-example") == 18


class SearchstringMustBeUneven(Exception):
    pass

def find_x_shaped(filename: str, searchstring: str = "MAS") -> int:
    grid, MAX_X, MAX_Y = open_file(filename)

    ans = 0

    def search_in_x(searchstring: str, coordinates: tuple[int, int]) -> bool:
        i = coordinates[0]
        j = coordinates[1]

        if (len(searchstring) % 2 == 0):
            raise SearchstringMustBeUneven

        center_char = searchstring[(len(searchstring)-1)//2:(len(searchstring)+2)//2]

        if grid[i][j] == center_char and 1 <= i < (MAX_Y - 1) and 1 <= j < (MAX_X - 1):
            # get corners
            uleft = grid[i-1][j-1]
            bright = grid[i+1][j+1]
            bleft = grid[i+1][j-1]
            uright = grid[i-1][j+1]

            diag_1 = ''.join([uleft, bright])
            diag_2 = ''.join([uright, bleft])

            if (diag_1 == 'SM' or diag_1 == 'MS') and (diag_2 == 'SM' or diag_2 == 'MS'):
                return True

        return False

    for i in range(MAX_Y):  # MAX_Y # loop through rows
        for j in range(MAX_X): # loop through each column in row
            if search_in_x(searchstring, (i, j)):
                ans +=1 

    return ans

def test_find_x_mas_example():
    assert find_x_shaped("day-4-example") == 9


if __name__ == "__main__":
    print(f"part 1: {find_searchstring("day-4-input")}")
    print(f"part 2: {find_x_shaped("day-4-input")}")
