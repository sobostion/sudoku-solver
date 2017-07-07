#!/usr/bin/python
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


# need a way of getting columns

def getColumns():
    
    columns = {}
    for k in range(0,9):
        columns[k] = []
    
    for i in range(0,9):
        for j in range(0,9):
            columns[i].append(rows[j][i])
    return columns

columns = getColumns()

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

blocks = getBlocks()

# now for actually solving the puzzle
#check which numbers we need to find in a row
def findMissingRowIndexes(row_num):
    absent_index = []
    count = 0
    for item in rows[row_num]:
        if item == None:
            absent_index.append(count)
        count+=1
    return absent_index


def possibleNumsRow(row_num):
    absent_nums = []
    possible_nums = {}
    # find absent numbers in row
    for number in range(1,10):
        if number not in rows[row_num]:
            absent_nums.append(number)
    # get indexes of absent numbers
    absent_index = findMissingRowIndexes(row_num) 
    # check each missing number's block for numbers in absent
    for missingIndex in absent_index:
    # find which block the number is in
        if row_num < 3:
        # first three blocks
            if missingIndex < 3:
                possible_nums[missingIndex] = [ x for x in absent_nums if x not in blocks[0] ]
            elif missingIndex < 6:
                # does block contain any absent numbers? if so, remove as possibility
                possible_nums[missingIndex] = [ x for x in absent_nums if x not in blocks[3] ]            
            elif missingIndex < 9:
                # block 6
                possible_nums[missingIndex] = [ x for x in absent_nums if x not in blocks[6] ]
        elif row_num < 6:
        # second row of blocks
            if missingIndex < 3:
                possible_nums[missingIndex] = [ x for x in absent_nums if x not in blocks[1] ]
            elif missingIndex < 6:
                possible_nums[missingIndex] = [ x for x in absent_nums if x not in blocks[4] ]
            elif missingIndex < 9:
                possible_nums[missingIndex] = [ x for x in absent_nums if x not in blocks[7] ]
        
        elif row_num < 9:
        # third row of blocks
            if missingIndex < 3:
                possible_nums[missingIndex] = [ x for x in absent_nums if x not in blocks[2] ]
            elif missingIndex < 6:
                possible_nums[missingIndex] = [ x for x in absent_nums if x not in blocks[5] ]
            elif missingIndex < 9:
                possible_nums[missingIndex] = [ x for x in absent_nums if x not in blocks[8] ]
    # at this point we have possible numbers when taking into account rows and blocks
    # now we need to take columns into account
    # each key of the possible_nums dictionary is a column nunber
    # we can remove any values that already exist in that column
    
    for column, possibles in possible_nums.items():
        # if columns[column] shares values with possibles, remove those values from possibles
        for number in possibles:
            if number in columns[column]:
                possibles.remove(number)
    
    return possible_nums

def enterAnswer():
    
    # enter values into rows
    for row in range(0,9):
        for column, possibles in possibleNumsRow(row).items():
            if len(possibles) == 1:
                 rows[row][column] = possibles[0]
    # reset blocks with new rows
    blocks = getBlocks()
    # if block has 1 missing value, fill it in
    for block in range(0,9):
        if blocks[block].count(None) == 1:
            # find missing number
            absent_num = [ x for x in range(1,10) if x not in blocks[block] ]
            # replace None with absent_num[0]
            blocks[block] = [ absent_num[0] if x is None else x for x in blocks[block] ]
    return 0

for i in range(0,10):
    try:
        for key, value in rows.items():
            print key, value

        enterAnswer()
        print " "
    except:
        break
