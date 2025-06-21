fin = open('Weekly Tests//june_3rd_week//ttttin.txt', 'r') # opening the input file
fout = open('Weekly Tests//june_3rd_week//ttttout.txt', 'w') # opening the file

matrix = [] # initiating matrix as an empty list, we are going to store the order and the values in matrix format, so that it will be easy to calculate
for i in range(3):
    line = fin.readline().strip() # reading lines from the file and strip is used to remove spaces and will be in form of string
    row = [] # initiating row as an empty list
    for char in line: # loop through each lines
        row.append(char)
    matrix.append(row) # append all the values to matrix

lines = []
for i in range(3):
    lines.append(matrix[i]) # append the rows from matrix to lines

for i in range(3):
    column = [matrix[0][i], matrix[1][i], matrix[2][i]] # append columns to lines
    lines.append(column)

diag1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
diag2 = [matrix[0][2], matrix[1][1], matrix[2][0]]
lines.append(diag1)
lines.append(diag2) # appending diagonals to lines

individual_winners = [] # initializing individual_winner as an empty list
team_winners = set()  # Using a set to avoid duplicates

for line in lines:
    unique = set(line) # the set will remove duplicate values, so that we are using set, here and storing them named as unique
    if len(unique) == 1: # if only one character for the complete line, then individually won the match
        individual_winners.append(line[0]) # so appending the value to individual_winners
    elif len(unique) == 2: # if there are two type of characters, then there is a chance to be a team winner
        pair = ''.join(sorted(unique))  # sorting, because if the outputs were like (a,b) and (b,a) then it will be seperate, so by sorting, we are making it same
        team_winners.add(pair)


fout.write(str(len(set(individual_winners)))) # writing the outputs
fout.write('\n')
fout.write(str(len(team_winners)))
fin.close() # closing the files
fout.close()