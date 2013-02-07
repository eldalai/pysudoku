'''
Created on 07/02/2013

@author: gabriel.flores
'''
import SudokuResolver

if __name__ == '__main__':
    print "Welcome to Sudoku Resolver!"
    print "Please enter the 9 lines of the problem"
    print "Each line have to have 9 numbers from 1 to 9"
    print "or  \"x\" for the unknowns numbers."
    #lines = "x34678912672195348198342567859761423426853791713924856961537284287419635345286179"    
    #lines = "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"
    lines = ""
    for i in range(9):
        line = raw_input("Enter line " + str(i+1) + " :")
        lines = lines + line
    print "Your answer is:    "    
    print SudokuResolver.resolve(lines)
    raw_input("Press enter to exit, thanks for play!")
    