with open('input.txt') as f:
    lines = f.readlines()

horizontal = 0
depth = 0

for line in lines:
    args = line.split(' ')
    if args[0] == 'forward':
        horizontal += int(args[1])
    elif args[0] == 'down':
        depth += int(args[1])
    elif args[0] == 'up':
        depth -= int(args[1])

solution = horizontal * depth
print(solution)


### Part 2

horizontal = 0
depth = 0
aim = 0

for line in lines:
    args = line.split(' ')
    if args[0] == 'forward':
        horizontal += int(args[1])
        depth += aim * int(args[1])
    elif args[0] == 'down':
        aim += int(args[1])
    elif args[0] == 'up':
        aim -= int(args[1])

solution = horizontal * depth
print(solution)