# tic tac toe
grid = [[0,0,0],
        [0,0,0],
        [0,0,0]]
condition = True
choose_x_o = input("You're first! Would you like to be X or O? ")
count = 1
while condition or count == 9: 
    row = int(input("what row do you want to do? "))
    col = int(input("what column want to do? "))
    if grid[row - 1][col - 1] == "x" or grid[row - 1][col - 1] == "o":
        print("that move has already been done")
        continue
    grid[row - 1][col - 1] = choose_x_o

    if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
        condition = False
        print("The winner is", + choose_x_o + "!")
    
    # check = 0 
    for i in range(len(grid)):
        row_count = 0
        col_count = 0
        for j in range(len(grid)):
            if grid[j][i] == grid[j+1][i]:
                col_count += 1
            elif grid[i][j] == grid[i][j+1]:
                row_count += 1
            if row_count == 2 or col_count == 2:
                condition = False
                print("The winner is", + choose_x_o + "!")  
         
    if choose_x_o == "x":
        choose_x_o = "o"
    else:
        choose_x_o = "x"
    count += 1
if count == 9:
    print("There was no winner of the game")