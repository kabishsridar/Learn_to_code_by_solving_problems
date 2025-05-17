wordin = open('wordin.txt', 'r') # opening the file in read mode 
wordout= open('wordout.txt', 'w') # opening the file in write mode
# the first line of file contains the number of words and the maximum number of characters per line
lines = wordin.readline().split() # read first line alone
max_char_per_line = int(lines[1])
wordlst = wordin.readline().split() # read the second line

line = ''
char_on_line = 0

for i in wordlst:
    if char_on_line + len(i) <= max_char_per_line: # if current word can fit in line, add it to the line with a space
        line += i + ' '
        char_on_line += len(i) + 1
    else:
        wordout.write(line[:-1] + '\n') # if current word cannot fit in the line, write the current line to the file wordout
        line = i + ' '
        char_on_line = len(i) + 1 
wordout.write(line[:-1] + '\n') # write the last line to the file wordout

wordin.close()
wordout.close()
#close the files
# the above code takes the input from wordin.txt and writes the output to wordout.txt
#download both the files named wordin.txt and wordout.txt in same path where this file is saved those are provided in the same repository