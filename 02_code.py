summa = 0
with open('02.txt') as f:
    for line in f:
        line = line.strip().split(' ')
        if line[1] == "X":
            summa += 1
            if line[0] == "A":
                summa += 3
            elif line[0] == 'C':
                summa += 6 
        elif line[1] == "Y":
            summa += 2
            if line[0] == "A":
                summa += 6
            elif line[0] == 'B':
                summa += 3
        else:
            summa += 3
            if line[0] == "B":
                summa += 6
            elif line[0] == 'C':
                summa += 3
    print(summa)