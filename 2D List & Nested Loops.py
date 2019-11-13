print("2D List & Nested Loops Start from 2:47 minute")
print("Example1")
number_grid = [
    [1,2,3,],
    [4,5,6,],
    [7,8,9,],
    [0]

]

print (number_grid[0][0])


print("Example2")
number_grid = [
    [1,2,3,],
    [4,5,6,],
    [7,8,9,],
    [0]

]

print (number_grid[2][1])



print("Example3")
number_grid = [
    [1,2,3,],
    [4,5,6,],
    [7,8,9,],
    [0]

]

for row in number_grid:
    print (row)

    print("Example4")
    number_grid = [
        [1, 2, 3, ],
        [4, 5, 6, ],
        [7, 8, 9, ],
        [0]

    ]

    for row in number_grid:
        for col in row:
            print(col)