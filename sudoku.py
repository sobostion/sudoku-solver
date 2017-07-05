# sudoku solver

# initialise sudoku puzzle
# let's convert this to a dictionary of lists

rows = {}

rows[1] = [2,5,3,4,None,6,None,None,None]
rows[2] = [6,None,7,None,3,8,5,4,1]
rows[3] = [None,None,None,9,5,None,2,None,None]
rows[4] = [None,None,None,None,None,None,None,9,4]
rows[5] = [None,6,None,None,None,None,None,3,None]
rows[6] = [8,7,None,None,None,None,None,None,None]
rows[7] = [None,None,2,None,7,3,None,None,None]
rows[8] = [9,1,6,5,4,None,3,None,7]
rows[9] = [None,None,None,6,None,9,4,1,2]

# finding solutions
# need a way of getting blocks

def makeBlock(first_row,second_row,third_row):
    
    # initialise blocks dictionary
    blocks = {}
    for i in range(1,10):
        blocks[i] = []

    # create blocks
    for i in range(0,3):
            blocks[1].extend( [ rows[1][i], rows[2][i], rows[3][i] ] )
    return blocks

print makeBlock(rows[1], rows[2], rows[3])
