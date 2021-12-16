import re

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
lines.remove(lines[0]) # Remove number draw line
lines = [x for x in lines if len(x) > 2] # Dirty \n removal
lines = [re.sub('\n', '', x) for x in lines] # Remove \n at end of row
lines = [re.sub(' +', ' ', x) for x in lines] # Remove multiple white spaces
lines = [x.strip() for x in lines] # Remove white space at the beginning
numbers = [re.sub('\n', '', x) for x in numbers] # Remove \n for the last number drawn

# Transform board array in a 5 chunk array (5x5 board)
sliced_arrs = list(chunks(lines, 5))

def get_winning_board():
    solutions = []
    finished_boards = []
    for drawn_index, drawn_number in enumerate(numbers):
        for board_index, board in enumerate(sliced_arrs):
            if board_index in finished_boards:
                continue

            for row_index, row in enumerate(board):
                for col_index, num in enumerate(row.split()):
                    if num == drawn_number:
                        # Update the game board
                        row = ' '.join(['x' if x == drawn_number else x for x in row.split()]).strip()
                        board[row_index] = row
                        sliced_arrs[board_index] = board
            
                # Win Check (Row-Check)
                if row == 'x x x x x':
                    remaining_numbers = []
                    for x in board:
                        for y in x.split():
                            if y != 'x':
                                remaining_numbers.append(y)
                    # Sum up the remaining numbers and multiply it with the last drawn number
                    solution = sum(map(int, remaining_numbers)) * int(drawn_number)
                    solutions.append(solution)
                    finished_boards.append(board_index)
                    break
                
                # Not sure if this works lol
                if row_index == 0:
                    for col_index, num in enumerate(row.split()):
                        if row[col_index] and board[row_index + 1][col_index] and board[row_index + 2][col_index] and board[row_index + 3][col_index] and board[row_index + 4][col_index] == 'x':
                             print(f'{board_index} Bingo')

solution = get_winning_board()
print(solution)