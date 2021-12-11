### Part 1
### Goal: Look how often the next number is bigger than the previous

with open('input.txt') as f:
    lines = f.readlines()

last_line = 0
count = 0

for line in lines:
    if int(line) > last_line:
        count += 1
    
    last_line = int(line)

# Ignore the first TRUE condition
print(count - 1)


### Part 2
### Goal:
### Take the first number and add the two following, save the sum
### Take the next number and add the two following, check if sum is bigger than the previous sum

last_sum = 0
solution = 0
for i in range(len(lines)):
    sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])

    if sum > last_sum:
        solution += 1

    last_sum = sum

    if i == 1997:
        break

# Ignore the first TRUE condition
print(solution - 1)