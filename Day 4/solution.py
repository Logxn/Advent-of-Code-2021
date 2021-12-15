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

for i in range(len(numbers)):
    if found:
        break

    wizzard.append(numbers[i])

    for arr in sliced_arrs:
        if found:
            break
        boards = np.reshape(arr, (1, 5))
        
        # Board-Logic
        # Loop over all boards
        for board in boards:
            for row_index in range(len(board)):
                row_numbers = board[row_index].split()
                for row_number_index in range(len(row_numbers)):
                    if row_numbers[row_number_index] == wizzard[i]:
                        row_numbers[row_number_index] = 'x'
                
                board[row_index] = ' '.join(row_numbers)
            
            # Row Check
            if any(elem == 'x x x x x' for elem in board):
                print('Bingo!')

        


                    
        

