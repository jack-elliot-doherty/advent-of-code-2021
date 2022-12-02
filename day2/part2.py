with open("input.txt") as f:
    forward = 0
    depth = 0
    aim = 0

    for line in f.readlines():
        line = line.strip().split()
        action = line[0]
        value = int(line[1])
        if action == "forward":
            forward += value
            depth += aim * value
        elif action == "down":
            aim += value  
        elif action == "up":
            aim -= value

print(forward * depth)