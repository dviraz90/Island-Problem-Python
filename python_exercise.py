import sys
from collections import deque

<<<<<<< HEAD

checked = set()
q = deque()

=======
>>>>>>> master
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

<<<<<<< HEAD

def addToQueue(i, j, grid):
    val = grid[i][j]
    if j+1 < len(grid[0]):
        if grid[i][j+1] == val and (i, j+1) not in checked:
            if [i, j+1] not in q:
                q.append([i, j+1])
    if j-1 >= 0:
        if grid[i][j-1] == val  and (i, j-1) not in checked:
            if [i, j-1] not in q:
                q.append([i, j-1])

    if i+1 < len(grid):
        if grid[i+1][j] == val and (i+1, j) not in checked:
            if [i+1, j] not in q:
                q.append([i+1, j])
    if i -1 >= 0:
        if grid[i-1][j] == val  and (i-1, j) not in checked:
            if [i-1, j] not in q:
                q.append([i-1, j])


def bfs(i,j,grid):
    addToQueue(i, j, grid)
    checked.add((i,j))
    if len(q) > 0:
        index = q.popleft()
        ni, nj = index[0], index[1]
        return bfs(ni,nj,grid)
    else:
        return 1
    
=======
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

>>>>>>> master

def findCountries(grid):
    countries = 0
    if check_numbers(grid) == False:
        return "please enter A valid LIST OF LIST N X M"
<<<<<<< HEAD
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if (i,j) not in checked:
                countries += bfs(i, j, grid)      
=======
    countries = 0
    val = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in check and grid[i][j] != 0:            
                right(i, j+1, grid)
                bottom(i, j, grid)           
                countries += 1
>>>>>>> master
    return countries

def convertStringToInt(l):
    row = []
    for i in l[1:]:
        col = []
        for n in i:
            try:    
                n = int(n)
                col.append(n)
            except ValueError:
                print("Please enter a valid matrix N X M with numbers 1-9 only ")   
                return False        
        row.append(col)
    return row

<<<<<<< HEAD
def main(args):
    print(findCountries(args))
            
=======
    for i in range(0,len(iputlist)):
        row.append(iputlist[i])
        for j in range(0,len(row[i])):
            if row[i][j] == ' ' or row[i][j] == "":
               continue
            row[i][j] = int(row[i][j])
    print(findCountries(row))

>>>>>>> master
if __name__ == '__main__':
    l = sys.argv[1:]
    args = convertStringToInt(l)
    if not args:
        exit(code=1)
    main(args)
