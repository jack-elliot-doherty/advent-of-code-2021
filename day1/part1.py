with open("input.txt") as f:
    
    prev = 0
    increased = -1
    for line in f.readlines():
        line = line.strip()
        if int(line) > prev:
            increased += 1
        prev = int(line)

print(increased)