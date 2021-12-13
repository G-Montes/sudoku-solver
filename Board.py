from typing import List


class Board:
    EMPTY = 0
    INVALID_INDEX = -1
    SECTION = {
        "ROW": 0,
        "COL": 1,
        "REGION": 2,
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

    def get_section(self, coord: tuple(int), section_type) -> List[int]:
        # TODO: Implement logic to get section for each type
        if section_type == self.SECTION["ROW"]:
            return self.board[coord[0]]
        elif section_type == self.SECTION["COL"]:
            section = []

            for row in self.board:
                section.append(row[coord[1]])

            return section
        else:
            section = []
            # Finds the starting (top left) indexes for the region coordinates are in
            region_start_row_coord = (
                coord[0] // self.region_row_size
            ) * self.region_row_size
            region_start_col_coord = (
                coord[1] // self.region_col_size
            ) * self.region_col_size

            for i in range(
                region_start_row_coord, region_start_row_coord + self.region_row_size
            ):
                for j in range(
                    region_start_col_coord, region_start_col_coord, self.region_col_size
                ):
                    section.append(self.board[i][j])

            return section

    def is_valid_section(section: List[int], check_complete: bool = False) -> bool:
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
            elif x != 0:
                invalid_list.append(x)

        return True

    def is_coord_valid(self, coord: tuple(int)) -> bool:
        """
        Returns True if the column, row, and region that the coordinate
        is in are considered valid sections.
        """

        if not self.is_valid_section(get_section(coord, self.SECTION["ROW"])):
            return False
        elif not self.is_valid_section(get_section(coord, self.SECTION["COL"])):
            return False
        elif not self.is_valid_section(get_section(coord, self.SECTION["REGION"])):
            return False

        return True
