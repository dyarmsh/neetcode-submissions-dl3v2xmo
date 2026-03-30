class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i, row in enumerate(board):
            row_set, col_set = set(), set()

            for j, cell in enumerate(row):
                # check row
                if row[j] != "." and row[j] in row_set:
                    return False
                row_set.add(cell)
            

                # check column
                if board[j][i] != "." and board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])


            
        # check sub-box 
        for x in range(0, 7, 3):
            for c in range(0, 7, 3):
                freq = set()
                for row in board[x:x+3]: 
                    for i in range(c, c+3): 
                        if row[i] != "." and row[i] in freq:
                            return False
                        freq.add(row[i])
            
        return True
