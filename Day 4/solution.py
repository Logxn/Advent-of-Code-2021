import re
import numpy as np

#https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

with open('input.txt') as f:
    lines = f.readlines()

numbers = lines[0].split(',')

# Filter
# We dont want empty lines
# We dont want random white spaces
# We dont want the random numbers to appear in list
lines.remove(lines[0])
lines = [x for x in lines if len(x) > 2]
lines = [re.sub('\n', '', x) for x in lines]
lines = [re.sub(' +', ' ', x) for x in lines]
lines = [x.strip() for x in lines]
numbers = [re.sub('\n', '', x) for x in numbers]


wizzard = []
sliced_arrs = list(chunks(lines, 5))
found = False

for drawn_number in numbers:
    for arr in sliced_arrs:
        boards = np.reshape(arr, (1, 5))

        for board_index, board in enumerate(boards):
            col_numbers = []
            for row_index, row in enumerate(board):
                for col_index, num in enumerate(row.split()):
                    if col_index == 0:
                        col_numbers.append(num)

                    if num == drawn_number:
                        # Update the game board
                        row = ' '.join(['x' if x == drawn_number else x for x in row.split()]).strip()
                        board[row_index] = row
                        boards[board_index] = board
            

        


                    
        

