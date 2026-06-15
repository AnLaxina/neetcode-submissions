from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r_index, row in enumerate(board):
            for c_index, val in enumerate(row):

                if val == ".":
                    continue

                if val in rows[r_index] or val in cols[c_index] or val in squares[(r_index // 3, c_index // 3)]:
                    return False 

                rows[r_index].add(val)
                cols[c_index].add(val)
                squares[(r_index // 3, c_index // 3)].add(val)
        
        return True