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
    
    blockList1 = []
    blockList2 = []
    blockList3 = []
    for i in range(0,3):
        blockList1.extend([first_row[i], second_row[i], third_row[i]])
    for i in range(3,6):
        blockList2.extend([first_row[i], second_row[i], third_row[i]])
    for i in range(6,9):
        blockList3.extend([first_row[i], second_row[i], third_row[i]])
    return blockList1, blockList2, blockList3
        

blocks1 = makeBlock(rows[1], rows[2], rows[3])
blocks2 = makeBlock(rows[4], rows[5], rows[6])
blocks3 = makeBlock(rows[7], rows[8], rows[9]) 
print blocks1, blocks2, blocks3
