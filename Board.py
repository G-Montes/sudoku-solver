from typing import List


class Board:
    """
    A class to represent a sudoku board.
    """

    EMPTY = 0
    INVALID_INDEX = -1
    SECTIONS = {
        "ROW": 0,
        "COL": 1,
        "REGION": 2,
    }

    def __init__(
        self, board: List[List[int]], region_row_size: int, region_col_size: int
    ):
        self.grid_size = len(board[0])
        self.region_row_size = region_row_size
        self.region_col_size = region_col_size
        self.board = board

    def print_unformatted_board(self) -> None:
        """
        Prints the board. Every row is on its own line.
        """
        for row in self.board:
            print(row)

    def find_next_empty_cell(self) -> "tuple[int, int]":
        """
        Returns a tuple containing the coordinates of the next EMPTY value.
        Otherwise, it returns a tuple containing INVALID_INDEX
        """
        j = self.INVALID_INDEX
        for i, row in enumerate(self.board):
            try:
                j = row.index(self.EMPTY)
            except ValueError:
                continue

            return (i, j)

        return (self.INVALID_INDEX, self.INVALID_INDEX)

    def get_section(self, row_index: int, col_index: int, section_type) -> List[int]:
        """
        Returns a list containing the row, column, or subregion of the coordinates provided.
        """
        if section_type == self.SECTIONS["ROW"]:
            return self.board[row_index]
        if section_type == self.SECTIONS["COL"]:
            return [row[col_index] for row in self.board]

        subregion = []
        # Finds the starting (top left) indexes for the region the provided coordinates are in
        region_start_row_index = (
            row_index // self.region_row_size
        ) * self.region_row_size
        region_start_col_index = (
            col_index // self.region_col_size
        ) * self.region_col_size

        for i in range(
            region_start_row_index, region_start_row_index + self.region_row_size
        ):
            for j in range(
                region_start_col_index,
                region_start_col_index + self.region_col_size,
            ):
                subregion.append(self.board[i][j])

        return subregion

    def is_valid_section(self, section: List[int], check_complete: bool) -> bool:
        """
        Returns True if the list contains unique natural numbers. Optional paramater
        that can be passed to check whether section contains ONLY unique natural numbers.
        """
        invalid_list = []
        # Allows this function to check if section is complete instead
        if check_complete:
            invalid_list.append(0)
        for x in section:
            if x in invalid_list:
                return False
            if x != 0:
                invalid_list.append(x)

        return True

    def is_coord_valid(
        self, coord: "tuple[int, int]", check_complete: bool = False
    ) -> bool:
        """
        Returns True if the column, row, and region that the coordinate
        is in are considered valid sections.
        """

        for section_type in self.SECTIONS.values():
            section = self.get_section(coord[0], coord[1], section_type)
            if not self.is_valid_section(section, check_complete):
                return False

        return True

    def solve_sudoku(self) -> bool:
        """
        Returns True if a solution has been found. Returns false otherwise.
        Implements a backtracking.

        Assigns a valid number to the next empty cell. Repeats until board complete.
        If no valid number possible for a cell, goes back to previous filled-in cell
        and tries a different valid number, repeats as necessary.
        """
        empty_cell = self.find_next_empty_cell()
        if empty_cell[0] == self.INVALID_INDEX:
            return True

        for i in range(1, self.grid_size + 1):
            self.board[empty_cell[0]][empty_cell[1]] = i

            if self.is_coord_valid(empty_cell) and self.solve_sudoku():
                return True
            self.board[empty_cell[0]][empty_cell[1]] = self.EMPTY

        return False


puzzle_arr = [
    [0, 0, 0, 4, 6, 0, 0, 3, 0],
    [3, 9, 0, 0, 0, 1, 7, 0, 5],
    [2, 8, 4, 0, 0, 0, 0, 9, 0],
    [5, 0, 0, 8, 7, 0, 6, 1, 3],
    [8, 3, 1, 0, 9, 0, 0, 0, 0],
    [0, 0, 2, 5, 1, 0, 0, 8, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 9],
    [4, 0, 5, 0, 2, 6, 3, 0, 0],
    [0, 0, 0, 0, 4, 7, 5, 6, 1],
]

puzzle = Board(puzzle_arr, 3, 3)
puzzle.print_unformatted_board()
print(puzzle.solve_sudoku())
puzzle.print_unformatted_board()
