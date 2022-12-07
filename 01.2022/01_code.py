with open('01.txt') as f:
    lines = f.readlines()

summa = 0
max_val = 0
for line in lines:
    # print(line)
    if line != '\n':
        summa += int(line.strip())
    else:
        if summa > max_val:
            max_val = summa
        summa = 0
print(max_val)