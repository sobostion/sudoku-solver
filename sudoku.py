# sudoku solver

# initialise sudoku puzzle
row1 = [2,5,3,4,None,6,None,None,None]
row2 = [6,None,7,None,3,8,5,4,1]
row3 = [None,None,None,9,5,None,2,None,None]
row4 = [None,None,None,None,None,None,None,9,4]
row5 = [None,6,None,None,None,None,None,3,None]
row6 = [8,7,None,None,None,None,None,None,None]
row7 = [None,None,2,None,7,3,None,None,None]
row8 = [9,1,6,5,4,None,3,None,7]
row9 = [None,None,None,6,None,9,4,1,2]

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
        

block1 = makeBlock(row1, row2, row3)
print block1
