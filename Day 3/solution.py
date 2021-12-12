import sys
sys.setrecursionlimit(10000) 


with open('input.txt') as f:
    lines = f.readlines()


gamma = ''
delta = ''

length = len(lines[0])
for i in range(0, length - 1):
    zero = 0
    one = 0

    for line in lines:
        if line[i] == '0':
            zero += 1
        else:
            one += 1
    
    if zero > one:
        gamma += '0'
    else:
        gamma += '1'

for c in gamma:
    if c == '0':
        delta += '1'
    else:
        delta += '0'
print(gamma)
print(delta)

solution = int(gamma, 2) * int(delta, 2)
print(f'Power Consumption: {solution}')

## Part 2

# Oxygen Generator Rating
def o2(input, start_index):
    length = len(input)
    
    if length == 1:
        return input[0]

    zero = 0
    one = 0

    # Determination of the most common bit    
    for line in input:
        if line[start_index] == '0':
            zero += 1
        else:
            one += 1

    if one > zero:
        new_input = [x for x in input if x[start_index] != '0']
        return o2(new_input, start_index + 1)
    elif zero > one:
        new_input = [x for x in input if x[start_index] != '1']
        return o2(new_input, start_index + 1)
    else:
        new_input = [x for x in input if x[start_index] != '0']
        return o2(new_input, start_index + 1)
    

# CO2 Scrubber Rating
def co(input, start_index):
    length = len(input)
    
    if length == 1:
        return input[0]

    zero = 0
    one = 0

    for line in input:
        if line[start_index] == '0':
            zero += 1
        else:
            one += 1
    
    if zero < one:
        new_input = [x for x in input if x[start_index] != '1']
        return co(new_input, start_index + 1)
    elif zero > one:
        new_input = [x for x in input if x[start_index] != '0']
        return co(new_input, start_index + 1)
    else:
        new_input = [x for x in input if x[start_index] != '1']
        return co(new_input, start_index + 1)


    
ox_rate = int(o2(lines, 0), 2)
co_rate = int(co(lines, 0), 2)

solution = ox_rate * co_rate
print(f'Life Support Rating: {solution}')

