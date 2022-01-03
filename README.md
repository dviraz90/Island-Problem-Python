# ** Island Problem **

## About the project

### Description
#### In this exercise, a two-dimensional matrix of positive integers represents a map of a
 continent that contains one or more countries. If two adjacent cells - adjacent either
horizontally or vertically - contain the same number, then they belong to the same country.
For example, the 5x6 matrix.
 
##### 1 1 1 2 3 3
##### 1 1 2 2 3 3
##### 1 2 1 1 3 3
##### 1 1 1 1 3 1
##### 2 2 3 3 4 1

represents a continent with 8 countries

the program takes its arguments from the command line.
### Prereqisites

    Python >= 3.0

### Usege

    python .\python_exercise.py --list  111233  112233  121133  111131  223341 
    or any  N X M matrix

### Docker Build 

    docker build -t python-exercise .

### Docker Run 

    docker run python-exercise

### Author

    Dvir azami:
        github@dviraz90
    

