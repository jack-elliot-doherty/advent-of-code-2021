with open("input.txt") as f:
    forward = 0
    depth = 0
    for line in f.readlines():
        line = line.strip().split()
        action = line[0]
        value = int(line[1])
        if action == "forward":
            forward += value
        elif action == "down":
            depth += value  
        elif action == "up":
            depth -= value

print(forward * depth)