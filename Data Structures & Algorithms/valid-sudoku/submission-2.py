class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i, row in enumerate(board):
            row_set = set()
            col_set = set()
            for j, cell in enumerate(row):
                
                # check row
                
                if row[j] != "." and row[j] in row_set:
                    return False
                row_set.add(cell)
                
                

                # check column
               
                if board[j][i] != "." and board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])
            print(row_set)
            print(col_set)

            
            # check sub-box
            
        for x in range(0, 7, 3):
            print(board[x:x+3])
            for c in range(0, 7, 3):
                freq = set()
                for row in board[x:x+3]: #0:3, 3:6, 6:9
                    # row[0] = 0 -> 3
                    # row[1] = 0 -> 3
                    # row[2] = 0 -> 3
                    
                    
                    
                        
                    for i in range(c, c+3): #0:3, 3:6, 6:9
                        print(row[i])
                        if row[i] != "." and row[i] in freq:
                            print("false 3")
                            return False
                            
                        freq.add(row[i])
                print(freq)
                print("--")
            
        return True


["1","2",".",".","3",".",".",".","."],
["4",".",".","5",".",".",".",".","."],
[".","9","1",".",".",".",".",".","3"],
["5",".",".",".","6",".",".",".","4"],
[".",".",".","8",".","3",".",".","5"],
["7",".",".",".","2",".",".",".","6"],
[".",".",".",".",".",".","2",".","."],
[".",".",".","4","1","9",".",".","8"],
[".",".",".",".","8",".",".","7","9"]