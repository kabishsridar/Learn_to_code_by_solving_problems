wordin = open('wordin.txt', 'r')
wordout= open('wordout.txt', 'w')

lines = wordin.readline().split()
max_char_per_line = int(lines[1])  # Max characters per line
wordlst = wordin.readline().split()

line = ''
char_on_line = 0

for i in wordlst:
    if char_on_line + len(i) <= max_char_per_line:
        line += i + ' '
        char_on_line += len(i) + 1
    else:
        wordout.write(line[:-1] + '\n')
        line = i + ' '
        char_on_line = len(i) + 1 
wordout.write(line[:-1] + '\n')

wordin.close()
wordout.close()
#download both the files named wordin.txt and wordout.txt in same path where this file is saved those are provided in the same repository
