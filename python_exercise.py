import sys
from collections import deque


checked = set()
q = deque()

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
    

def findCountries(grid):
    countries = 0
    if check_numbers(grid) == False:
        return "please enter A valid LIST OF LIST N X M"
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if (i,j) not in checked:
                countries += bfs(i, j, grid)      
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

def main(args):
    print(findCountries(args))
            
if __name__ == '__main__':
    l = sys.argv[1:]
    args = convertStringToInt(l)
    if not args:
        exit(code=1)
    main(args)
