
def find_xmas(filename: str, searchstring: str = "XMAS"):
    with open(filename, "r") as input:
        grid = [list(line.rstrip()) for line in input.readlines()]

    MAX_X = len(grid[0]) -1
    MAX_Y = len(grid) - 1 
    
    ans = 0

    # build direction vectors
    dir_vectors = []
    for dcol in range(-1, 2):
        for drow in range(-1, 2):
            if not drow == dcol == 0:
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

    def search_in_direction(vector: tuple[int, int], searchstring: str, verbose: bool = False) -> bool:
        coordinates_found = []

        for steps, target_char in enumerate(searchstring):
            ii = i + steps * vector[1]
            jj = j + steps * vector[0]

            if not (0 <= ii < MAX_Y and 0 <= jj < MAX_X):
                return False
            
            if grid[ii][jj] != target_char:
                return False
            
            coordinates_found.append((ii, jj))

        print(coordinates_found)
        return True

    for i in range(MAX_Y):  # MAX_Y # loop through rows
        for j in range(MAX_X): # loop through each column in row
            for vector in dir_vectors:
                if search_in_direction(vector, searchstring):
                    ans +=1 
                if search_in_direction(vector, searchstring[::-1], True):
                    ans +=1 


    print(ans)

