from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r_index, row in enumerate(board):
            for c_index, value in enumerate(row):
                if value == ".":
                    continue
                    
                if value in rows[r_index] or value in cols[c_index] or value in squares[(r_index // 3, c_index // 3)]:
                    return False
                
                rows[r_index].add(value)
                cols[c_index].add(value)
                squares[(r_index // 3, c_index // 3)].add(value)
        
        return True