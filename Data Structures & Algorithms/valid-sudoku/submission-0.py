class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                # check row
                if cell != "." and (cell in row[:j] or cell in row[j+1:]):
                    print("false 1")
                    return False

                # check column
                if cell != ".":
                    for k in range(8):
                        if k != i:
                            if cell == board[k][j]:
                                print("false 2")
                                return False

            
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