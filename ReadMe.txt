I want this to be a sudoku solver. For the base program, I want it to be
able to solve any 9x9 puzzles using backtracking. Other features I would 
like to incude:

@1 Sudoku image extractor
    -I want to be able to pass an image with either a solved or unsolved 
     puzzle and have the numbers extracted into an array that the solver 
     can use to attempt a solve.

@2 Solution verification
    -There's a folder that contains puzzles and their respective
     solutions. The program should fetch the corresponding solution image,
     extract the numbers, and verify that the array matches those of the 
     solution image.
    
    -Alternatively, at the end of the solve, I want an alternative 
     verification by checking column, row, region.
        -The reasoning for this is because not all sudoku puzzles have a 
         unique solution. Eventually, I might transition to a database for
         handling sudoku puzzles. If a user discovers a new solution, then
         I would like to add it to the databse as a viable solution for 
         that puzzle.

@3 Select a solution method
    -I want to be able to select which algorithm is used to solve the
     puzzles.
        -The only concrete algorithm I use backtracking for now.

@4 Have a visualized board for the problem and the solution
    -At the beggining, create and display a board that shows the attempted
     puzzle (This should be generated, not use the boards from where the 
     puzzle is retrieved).

@5 Visualize the algorithm at every step
    -Every time a number is selected by the algorithm, it should display 
     the change on the board. That way a person looking at the program can
     visualize the process.

@6 Keep track of specific data
    -The program should keep track of time elapsed from starting the 
     algorithm, to finding a solution.
    -Maybe keep track of the number of times a change is made to the board.

@7 Enable concurrent solutions
    -Allow for the program to be able to solve the same puzzle 
     concurrently. This could be some or all of the algorithms and the 
     same functionality should be offered as if it were only one 
     algorithm run.

@8 Create a database that contains the Sudoku images and the board in 
    array from
    -I would like to have it so the user doesn't need to have a copy of 
     the images in order to use the program. Eventually, I want to do the
     following:
        -Have the user select a puzzle or randomly select one.
        -Find both the selected puzzle and its respective solution.
        -For both, extract the numbers from the image into an array.** 
        -Upload the arrays into the database so that next time the puzzle
         is selected the image extraction isn't needed.
        -Either allow the user to attempt the solution, or use the sudoku 
         solver to generate the solution.
        -If the solver's solution doesn't match the solution in the database,
         but is still a valid solve, upload the alternative solution to the
         database. Next time the puzzle is selected, the solution found will
         be compared to all known solutions for that particular puzzle, and
         the puzzle is repeated.

        ** It would probably be better for the user if the image processing
         for all images was done prior. That way, when the user selects a 
         puzzle, the extraced numbers are already present in the database. 
         This means the user has less of a wait time in order to get access 
         to puzzle. 