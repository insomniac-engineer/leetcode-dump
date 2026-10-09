class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1 cycle - check all rows
        # 2 cycle - check all columns
        # 3 cycle - check all quarters

        # Check rows
        duplicate_el = set()

        for row in board:
            for el in row:
                if el == ".": continue
                if el in duplicate_el:
                    return False
                duplicate_el.add(el)
            duplicate_el.clear()

        # Check cols
        for idx_c, col in enumerate(board):
            for el in board:
                if el[idx_c] == ".": continue
                if el[idx_c] in duplicate_el:
                    return False
                duplicate_el.add(el[idx_c])
            duplicate_el.clear()

        dup_dict = defaultdict(set)
        # Check quarters
        for idx_c, col in enumerate(board):
            for idx_r, el in enumerate(col):
                if el == ".": continue
                quarter = (idx_r//3, idx_c//3)
                if el in dup_dict[quarter]:
                    return False
                dup_dict[quarter].add(el)
        return True