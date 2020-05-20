I want this to be a sudoku solver. For the base program, I want it 
to be able to solve any 9x9 puzzles using backtracking. Other features
I would like to incude:

- @1 Sudoku image extractor
    -I want to be able to pass an image with either a solved or unsolved puzzle
     and have the numbers extracted into a list that the solver can unsolved

- @2 Solution verification
    -There's a file that contains puzzles and their respective solutions. The program
     should fetch the corresponding solution image, extract the numbers, and verify
      that the array matches those of the solution image
    
    -Alternatively, at the end, I want it to verify manually by checking column, row, 
     region

- @3 Select a solution method
    -I want to be able to select which algorithm is used to solve the puzzles

- @4 Have a visualized board for the problem and the solution. 
    -At the beggining, create and display a board that shows the attempted puzzle 
     (this should be generated, not use the boards from where the puzzle is retrieved)

- @5 Visualize the algorithm at every step
    -Every time a number is selected by the algorithm, it should display the change on
     the board. That way a person looking at the program can visualize the process.

- @6 Keep track of specific data
    -The program should keep track of time elapsed from starting the algorithm, to finding 
     a solution
    -Maybe keep track of the number of times a change is made to the board

- @7 Enable concurrent solutions
    -Allow for the program to be able to solve the same puzzle concurrently. This could
     be some or all of the algorithms and the same functionality should be offered as if
     it were only one algorithm run