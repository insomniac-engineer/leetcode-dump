class Solution:
    def checkDirections(self, coordinate, grid, to_visit, seen) -> None:
        idx_r = coordinate[0]
        idx_c = coordinate[1]
        # check left/right
        if idx_c > 0: # edge case when we're in idx_c = 0
            if grid[idx_r][idx_c - 1] == "1" and (idx_r,idx_c - 1) not in seen:
                to_visit.add((idx_r, idx_c - 1))
        if idx_c + 1 != len(grid[0]): # edge case idx_c out of boundary
            if grid[idx_r][idx_c + 1] == "1" and (idx_r,idx_c + 1) not in seen:
                to_visit.add((idx_r, idx_c + 1))
        # check down/up
        if idx_r > 0: # edge case when we're in idx_c = 0
            if grid[idx_r - 1][idx_c] == "1" and (idx_r - 1,idx_c) not in seen:
                to_visit.add((idx_r - 1, idx_c))
        if idx_r < len(grid) - 1: # edge case idx_c out of boundary
            if grid[idx_r + 1][idx_c] == "1" and (idx_r + 1,idx_c)  not in seen:
                to_visit.add((idx_r + 1, idx_c))
        seen.add((idx_r, idx_c))
    def numIslands(self, grid: List[List[str]]) -> int:
        # (0,0) ->1
        # (0,1) -> 1
        # (0,2) -> 1
        islands = 0 
        seen = set()
        to_visit = set()
        for idx_r, row in enumerate(grid):
            for idx_c, el in enumerate(row):
                if el == "1" and (idx_r, idx_c) not in seen:
                    islands += 1
                    to_visit.add((idx_r, idx_c))
                    while len(to_visit) > 0:
                        # pop will return tuple and delete it
                        self.checkDirections(to_visit.pop(), grid, to_visit, seen)
        return islands