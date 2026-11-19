class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows unique
        for row in board:
            unique_row = set()
            for column in row:
                if column == ".": continue
                if column in unique_row:
                    return False
                unique_row.add(column)

        # check column unique
        for column_idx in range(len(board[0])): # [0 - 9)
            unique_column = set()
            for row in board:
                if row[column_idx] == ".": continue
                if row[column_idx] in unique_column:
                    return False
                unique_column.add(row[column_idx])

        # (colum // 3, row // 3)
        # (5//3, 2//3) -> (1, 0)
        # (4//3, 1//3) -> (1, 0)

        quadrant = defaultdict(set)

        for row_idx, row in enumerate(board):
            for col_idx, col_val in enumerate(row):
                if col_val == ".": continue
                if col_val in quadrant[(row_idx // 3, col_idx // 3)]:
                    return False
                quadrant[(row_idx // 3, col_idx // 3)].add(col_val)

        return True