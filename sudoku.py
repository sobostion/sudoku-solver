# sudoku solver

# initialise sudoku puzzle
# let's convert this to a dictionary of lists

rows = {}

rows[0] = [2,5,3,4,None,6,None,None,None]
rows[1] = [6,None,7,None,3,8,5,4,1]
rows[2] = [None,None,None,9,5,None,2,None,None]
rows[3] = [None,None,None,None,None,None,None,9,4]
rows[4] = [None,6,None,None,None,None,None,3,None]
rows[5] = [8,7,None,None,None,None,None,None,None]
rows[6] = [None,None,2,None,7,3,None,None,None]
rows[7] = [9,1,6,5,4,None,3,None,7]
rows[8] = [None,None,None,6,None,9,4,1,2]

# finding solutions
# need a way of getting blocks

def getBlocks():
    
    # initialise blocks dictionary
    blocks = {}
    for i in range(0,9):
        blocks[i] = []

    # create blocks
    for i in range(0,3):
        for j in range(0,9,3):
            blocks[j+0].extend( [ rows[0][i+j], rows[1][i+j], rows[2][i+j] ] )
            blocks[j+1].extend( [ rows[3][i+j], rows[4][i+j], rows[5][i+j] ] )
            blocks[j+2].extend( [ rows[6][i+j], rows[7][i+j], rows[8][i+j] ] )
    return blocks

print getBlocks()

# now for actually solving the puzzle
absent = []
absent_index = []
count = 0
#check which numbers we need to find in a row
for item in rows[0]:
    if item == None:
        absent_index.append(count)
    count+=1
print absent_index
 
