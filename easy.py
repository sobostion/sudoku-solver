#!/usr/bin/python
# sudoku solver
from prettytable import *
# initialise sudoku puzzle
rows = {}

rows[0] = [None, None, 2, None, 7, 5, None, 1, 3]
rows[1] = [None, None, None, None, None, None, 4, None, 9]
rows[2] = [7, None, 9, None, 4, None, 8, 2, None]
rows[3] = [3, None, 1, None, 9, 6, None, None, None]
rows[4] = [6, None, None, 3, None, 7, None, None, 1]
rows[5] = [None, None, None, 5, 8, None, 3, None, 6]
rows[6] = [None, 6, 4, None, 3, None, 5, None, 8]
rows[7] = [2, None, 5, None, None, None, None, None, None]
rows[8] = [8, 9, None, 1, 5, None, 7, None, None]

# need a way of getting columns


def getColumns():
    columns = {}
    for k in range(0, 9):
        columns[k] = []
    for i in range(0, 9):
        for j in range(0, 9):
            columns[i].append(rows[j][i])
    return columns


columns = getColumns()

# need a way of getting blocks


def getBlocks():
    # initialise blocks dictionary
    blocks = {}
    for i in range(0, 9):
        blocks[i] = []

    for k in [0, 3, 6]:
        j = 0
        for i in [0, 3, 6]:
            blocks[k + j] += rows[k][i:i + 3] + \
                rows[k + 1][i:i + 3] + rows[k + 2][i:i + 3]
            j = j + 1
    return blocks


blocks = getBlocks()

# now for actually solving the puzzle
# check which numbers we need to find in a row


def findMissingRowIndexes(row_num):
    absent_index = []
    count = 0
    for item in rows[row_num]:
        if item == None:
            absent_index.append(count)
        count += 1
    return absent_index


def possibleNumsRow(row_num):
    absent_nums = []
    possible_nums = {}
    # find absent numbers in row
    for number in range(1, 10):
        if number not in rows[row_num]:
            absent_nums.append(number)
    # get indexes of absent numbers
    absent_index = findMissingRowIndexes(row_num)
    blocks = getBlocks()    # reset blocks
    for missingIndex in absent_index:
        # find which block the number is in
        if row_num < 3:
            # first three blocks
            if missingIndex < 3:
                possible_nums[missingIndex] = [
                    x for x in absent_nums if x not in blocks[0]]
            elif missingIndex < 6:
                possible_nums[missingIndex] = [
                    x for x in absent_nums if x not in blocks[1]]
            elif missingIndex < 9:
                possible_nums[missingIndex] = [
                    x for x in absent_nums if x not in blocks[2]]
        elif row_num < 6:
            # second row of blocks
            if missingIndex < 3:
                possible_nums[missingIndex] = [
                    x for x in absent_nums if x not in blocks[3]]
            elif missingIndex < 6:
                possible_nums[missingIndex] = [
                    x for x in absent_nums if x not in blocks[4]]
            elif missingIndex < 9:
                possible_nums[missingIndex] = [
                    x for x in absent_nums if x not in blocks[5]]
        elif row_num < 9:
            # third row of blocks
            if missingIndex < 3:
                possible_nums[missingIndex] = [
                    x for x in absent_nums if x not in blocks[6]]
            elif missingIndex < 6:
                possible_nums[missingIndex] = [
                    x for x in absent_nums if x not in blocks[7]]
            elif missingIndex < 9:
                possible_nums[missingIndex] = [
                    x for x in absent_nums if x not in blocks[8]]
    # at this point we have possible numbers when taking into account  blocks
    # now we need to take columns into account
    # each key of the possible_nums dictionary is a column nunber
    # we can remove any values that already exist in that column
    columns = getColumns()  # reset columns for when function is used again
    for column, possibles in possible_nums.items():
        possible_nums[column] = [
            x for x in possibles if x not in columns[column]]
    return possible_nums


def blockIndex2Row(block, index):
    row_num = 0  # reset
    for i in [0, 3, 6]:
        if block in [i, i + 1, i + 2]:
            for j in [0, 3, 6]:
                if index in [j, j + 1, j + 2]:
                    return row_num  # we have found the row
                else:
                    row_num += 1  # not this row, try next row
        else:
            row_num += 3


def enterAnswer():
    # enter values into rows
    # if only 1 possible in row, fill in
    for row in range(0, 9):
        for column, possibles in possibleNumsRow(row).items():
            if len(possibles) == 1:
                rows[row][column] = possibles[0]
    # fill in columns with only one left
    columns = getColumns()
    for column in range(0, 9):
        if columns[column].count(None) == 1:
            index = columns[column].index(None)  # also the row number
            absent_num = [x for x in range(1, 10) if x not in columns[column]]
            rows[index][column] = absent_num[0]

    # reset blocks with new rows
    blocks = getBlocks()
    # if block has 1 missing value, fill it in
    for block in range(0, 9):
        if blocks[block].count(None) == 1:
            index = blocks[block].index(None)
            absent_num = [x for x in range(1, 10) if x not in blocks[block]]
            # at this point the block has been filled, but we still need to update the value in rows
            # otherwise getBlocks() will reset to the original blocks
            # we know the index of the None and can translate this to row/column
            row_num = blockIndex2Row(block, index)
            # let's update the row with the new value
            # there could be multiple None values per row, so we must be careful
            # we have to make sure the None is the one inside this block when we replace it

            # let's get the indexes of all the None values
            none_index = [i for i, j in enumerate(rows[row_num]) if j == None]

            if block in [0, 3, 6]:
                none_index = [x for x in none_index if x < 3]
            if block in [1, 4, 7]:
                none_index = [x for x in none_index if x > 2 and x < 6]
            if block in [2, 5, 8]:
                none_index = [x for x in none_index if x > 5 and x < 9]

            rows[row_num][none_index[0]] = absent_num[0]

    return 0


def noneCount():
    # counts how many empty squares are left
    count = 0
    for i in range(0, 9):
        for item in rows[i]:
            if item == None:
                count += 1
    return count


def prettyPrint():
    columns = getColumns()
    table = PrettyTable()
    table.hrules = ALL
    table.add_column(" ", range(0, 9))
    for i in [str(x) for x in range(0, 9)]:
        table.add_column(i, columns[int(i)])
    return table


def results():

    #    print "ORIGINAL"
    #    print prettyPrint()
    rows_before = 0  # initialise with different values,
    rows_after = 1  # doesn't matter what they are
    while(rows_before != rows_after):
        rows_before = noneCount()
        enterAnswer()
        rows_after = noneCount()
    print "FINAL"
    print prettyPrint()


results()
for i in range(0, 9):
    print i, possibleNumsRow(i)
