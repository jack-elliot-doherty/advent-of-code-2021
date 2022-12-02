with open("input.txt") as f:
    
    prev = 0
    increased = -1
    lines = f.readlines()

    for i in range(2,len(lines)):
        group_total =  int(lines[i-2]) + int(lines[i-1]) + int(lines[i])
        if group_total > prev:
            increased += 1
        prev = group_total

print(increased)