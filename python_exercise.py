import argparse


def check_numbers(grid):
    size = len(grid[0])
    for l in grid:
        if len(l) != size:
            return False
        for num in l:
            if num == ' ':
                continue
            num=int(num)
            if num < 1 or type(num) != int:
                return False
    return True

check = set()

def right(i, j, grid):
    if j in range(len(grid[0])-1):
        if grid[i][j+1] == grid[i][j]:
            if (i, j) not in check:
                check.add((i, j))
            check.add((i, j+1))
            bottom(i+1, j, grid)
            top(i, j, grid)
            left(i, j, grid)
            grid[i][j] = 0
            return right(i, j+1, grid)
    return


def left(i, j, grid):
    if j > 0:
        if grid[i][j-1] == grid[i][j]:
            if (i, j) not in check:
                check.add((i, j))
            check.add((i, j-1))
            grid[i][j] = 0
            return left(i, j-1, grid)
    return 


def top(i, j, grid):
    if i > 0:
        if grid[i-1][j] == grid[i][j]:
            if (i, j) not in check:
                check.add((i, j))
            check.add((i-1, j))
            left(i, j-1, grid)
            right(i, j+1, grid)
            grid[i][j] = 0
            return top(i-1, j, grid)
    return 0


def bottom(i, j, grid):
    if i in range(0,len(grid)-1):
        if grid[i+1][j] == grid[i][j]:
            if (i, j) not in check:
                check.add((i, j))
            check.add((i+1, j))
            right(i, j, grid)
            left(i+1, j, grid)
            top(i, j, grid)
            grid[i][j] = 0
            return bottom(i+1, j, grid)
    return 0


def findCountries(grid):
    if check_numbers(grid) == False:
        return "please enter A valid LIST OF LIST N X M"
    countries = 0
    val = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in check and grid[i][j] != 0:            
                right(i, j+1, grid)
                bottom(i, j, grid)           
                countries += 1
    return countries


def main(args):
    iputlist = []
    row = []
    for _, val in args._get_kwargs():
        if val is not None:
            for v in val:
                iputlist.append(v)

    for i in range(0,len(iputlist)):
        row.append(iputlist[i])
        for j in range(0,len(row[i])):
            if row[i][j] == ' ' or row[i][j] == "":
               continue
            row[i][j] = int(row[i][j])
    print(findCountries(row))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="countries in a list of a list")
    parser.add_argument("--list", nargs="+", type=list)
    args = parser.parse_args()
    main(args)
