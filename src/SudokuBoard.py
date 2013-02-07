'''
Created on 07/02/2013

@author: gabriel.flores
'''

class SudokuBoard(object):
    '''
    classdocs
    '''
    MAX_LENGHT = 9
    board = [ [ 0 for fil in xrange(MAX_LENGHT) ] for col in xrange(MAX_LENGHT) ]


    def __init__(self, initialBoard):
        '''
        Constructor
        '''

        x1 = 0
        for ifil in range(self.MAX_LENGHT): 
            for icol in range(self.MAX_LENGHT):
                number = initialBoard[x1:x1+1]
                self.board[ifil][icol] = int(number) 
                x1 = x1 + 1
        
    def isValid(self):    
        return self.isColsValid() & self.isFilsValid() & self.isSectorsValid()
    
    def toString(self):
        output = ""
        for col in range(self.MAX_LENGHT):
            for fil in range(self.MAX_LENGHT):
                output = output + str( self.board[fil][col] ) 
            output = output + "\n"
        return output        
    
    def isColsValid(self):
        ctl = [ 0 for xctl in xrange(self.MAX_LENGHT + 1) ]
        
        for col in range(self.MAX_LENGHT):
            for xctl in range(self.MAX_LENGHT+1):
                ctl[xctl] = 0
            for fil in range(self.MAX_LENGHT):
                if self.board[fil][col] != 0:
                    ctl[ self.board[fil][col] ] = ctl[ self.board[fil][col] ] + 1
                    if ctl[ self.board[fil][col] ] > 1:
                        #print "Ctrl x col: Invalid in: "+str(fil)+" col: "+str(col)+" num: " + str(self.board[fil][col])
                        return False
        return True
    
    def isFilsValid(self): 
        ctl = [ 0 for xctl in xrange(self.MAX_LENGHT + 1) ]
        
        for fil in range(self.MAX_LENGHT):
            for xctl in range(self.MAX_LENGHT+1):
                ctl[xctl] = 0
            for col in range(self.MAX_LENGHT):
                if self.board[fil][col] != 0:
                    ctl[ self.board[fil][col] ] = ctl[ self.board[fil][col] ] + 1
                    if ctl[ self.board[fil][col] ] > 1:
                        #print "Ctrl x fil: Invalid in: "+str(fil)+" col: "+str(col)+" num: " + str(self.board[fil][col])
                        return False
        return True
    
    def isSectorsValid(self):
        ctl = [ 0 for xctl in xrange(self.MAX_LENGHT + 1) ]
        
        for col in range(3):
            for fil in range(3):
                for xctl in range(self.MAX_LENGHT+1):
                    ctl[xctl] = 0
                for icol in range(3):
                    for ifil in range(3):
                        if self.board[fil*3+ifil][col*3+icol] != 0:
                            ctl[ int( self.board[fil*3+ifil][col*3+icol] ) ] = ctl[ int( self.board[fil*3+ifil][col*3+icol] ) ] + 1
                            if ctl[ int( self.board[fil*3+ifil][col*3+icol] ) ] > 1:
                                #print "Ctrl x sector: Invalid in fil:"+str(fil)+" col:"+str(col)+" num:"+str( self.board[fil*3+ifil][col*3+icol] );
                                return False

        return True
    
    def getCell(self, fil, col):
        return self.board[fil][col]

    def setCell(self, fil, col, candidate):
        self.board[fil][col] = candidate
