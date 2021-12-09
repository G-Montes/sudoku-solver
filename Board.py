from typing import List


class Board:
    EMPTY = 0
    INVALID_INDEX = -1
    SECTION = {
        ROW: "row",
        COL: "column",
        REGION: "region",
    }

    grid_size: int
    region_row_size: int
    region_col_size: int
    board: List[[int]]

    def __init__(self, board: List[[int]], region_row_size: int, region_col_size: int):
        self.grid_size = board.length()
        self.region_row_size = region_row_size
        self.region_col_size = region_col_size
        self.board = board

    def print_unformatted_board(self) -> None:
        """
        Prints the board. Every row is on its own line.
        """
        for row in self.board:
            print(row)

    def find_next_unsolved_cell(self) -> tuple(int):
        """
        Returns a tuple containing the coordinates of the next EMPTY value.
        Otherwise, it returns a tuple containing INVALID_INDEX
        """
        for i, row in enumerate(self.board):
            try:
                x_val = row.index(self.EMPTY)
            except ValueError:
                pass

            return (i, x_val)

        return self.INVALID_INDEX

    def get_section(self, section_type) -> List[int]:
        if section_type == self.SECTION[ROW]:
            pass
        elif section_type == self.SECTION[COL]:
            pass

    def is_valid_section(section: List[int]) -> bool:
        """
        Returns True if the list contains all unique natural numbers.
        """
        invalid_list = []

        for x in section:
            if x in invalid_list:
                return False
            else:
                invalid_list.append(x)

        return True

    def is_coord_valid(self, coord: tuple(int)) -> bool:
        """
        Returns True if the column, row, and region that the coordinate
        is in are considered valid sections.
        """

        if not self.is_valid_section(get_section(self.SECTION[ROW])):
            return False
        elif not self.is_valid_section(get_section(self.SECTION[COLUMN])):
            return False
        elif not self.is_valid_section(get_section(self.SECTION[REGION])):
            return False

        return True
