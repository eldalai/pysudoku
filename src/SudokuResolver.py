'''
Created on 07/02/2013

@author: gabriel.flores
'''
from SudokuBoard import SudokuBoard

def resolve(sudokuStr):
        sudokuStr = sudokuStr.replace("x", "0")
        
        board = SudokuBoard(sudokuStr)
        if board.isValid() == False: 
            print  "The board is not valid, give me a break!"
#        
        think(board, 0, 0);
        
        return board.toString()

    
#    /**
#     * think about posible answers... 
#     * @return true if it's resolved! false... should think better!  
#     */

def think(board, fil, col):
#        // the big end! return true to close the recursion
        if fil == SudokuBoard.MAX_LENGHT:
            return True;
#        // if is not empty, go on with others cells....
        if board.getCell( fil, col ) != 0:
            return goOn( board, fil, col )
#        
#        // try with all candidate numbers
        for candidate in range(9):
#            // set the board with the candidate...
            board.setCell( fil, col, candidate + 1 );
#            // if it is valid... onGo! THink another cell
            if( board.isValid() ):
                if goOn( board, fil, col ):
                    return True
#        // if wrong, go back to cero... other recursion gonna think better...
        board.setCell( fil, col, 0 )
        return False;

def goOn( board, fil, col):
    if col == SudokuBoard.MAX_LENGHT - 1 :
        return think( board, fil + 1, 0 )
    else:
        return think( board, fil, col + 1 )
